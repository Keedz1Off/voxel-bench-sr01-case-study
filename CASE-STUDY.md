# Voxel Bench SR-01: first-observer authorship capture

## Executive Summary

Mallory, using her own wallet, could observe Alice's unclaimed recipe ID and register it first in Voxel Bench's `RecipeBook`. The contract would record Mallory as author, reject Alice's later claim, and direct future craft fees for that ID to Mallory. The missing boundary was permission to claim Alice's recipe; no stolen key or forged signature was required.

I reviewed the vulnerable source, introducing changes, implemented fix, public test records and regression source. I did not run new target tests or make live chain calls for this report. The direct attack has a preserved successful PoC record; the signed variant is supported by source and subsequent regression coverage.

No release tags were returned by the upstream tag check, so these are verified source snapshots, not a claimed release range:

| Role | Commit |
|---|---|
| Direct publication introduced | `e1e531304b711462de9977fd0ab849b8f7ecd504` |
| Signed publication introduced | `75e6434167e6aa98f89c316f370cae47bb15026a` |
| Assessed vulnerable snapshot | `5015954e807783a9d6e68cff07984ce98556cfa0` |
| Implemented fix | `ba067ec240835cbc9e03bb991e644b75a1f30eb6` |

## Background

Voxel Bench associates a content-derived recipe ID with an author and credits that author when someone pays to craft it. Alice is the legitimate creator; Mallory knows the ID before registration and can submit a transaction that executes first. The historical harness exercised Solidity contracts locally; it did not establish an exploit across the web application or production deployments.

The signed route was introduced to let authors claim without paying gas themselves. Its EIP-712 message binds the ID and author to a contract and chain. Those bindings authenticate wallet consent, but cannot establish who created the recipe. [Introducing signed publication](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/commit/75e6434167e6aa98f89c316f370cae47bb15026a).

## Vulnerability Details

At the assessed snapshot, Mallory supplies Alice's unclaimed ID to `publish`. In `contracts/src/RecipeBook.sol`, the complete direct entry point is:

```solidity
function publish(bytes32 recipeId) external {
    _publish(recipeId, msg.sender);
}
```

The shared registration function checks only whether somebody already claimed that ID:

```solidity
function _publish(bytes32 recipeId, address author) internal {
    if (recipes[recipeId].author != address(0)) revert AlreadyPublished();
    recipes[recipeId].author = author;
    emit RecipePublished(recipeId, author);
}
```

Thus Mallory's first transaction makes her the recorded author; the same guard subsequently blocks Alice. The signed entry point has the same gap after validating the claimant's signature:

```solidity
if (_recover(digest, signature) != author) revert InvalidSignature();

_publish(recipeId, author);
```

Mallory can legitimately sign a message naming herself. Substitution checks protect Alice's signature from modification, but do not reject Mallory's independent claim. Finally, `craft` reads the stored author and credits that address:

```solidity
address author = recipe.author;
// Fee calculation and accounting omitted.
vault.credit{value: toAuthor}(author);
```

These excerpts are from the [assessed RecipeBook source](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/5015954e807783a9d6e68cff07984ce98556cfa0/contracts/src/RecipeBook.sol). The direct registration rule entered with the [initial economy implementation](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/commit/e1e531304b711462de9977fd0ab849b8f7ecd504); the later gasless route preserved first-claim registration.

## Exploitability Analysis

The primitive is capture of an unregistered author record, followed by misdirected future author credits. Mallory needs the correct ID, transaction access and favorable ordering. Already registered recipes are protected from replacement. The evidence does not establish a reliable mempool race, historical financial loss or theft of existing vault balances.

The historical control shows that relaying Alice's valid signature credits Alice, even when Mallory relays it. This rules out simple relayer substitution as the mechanism. The vulnerability is Mallory submitting her own claim first. Hiding unclaimed IDs reduces exposure, but does not authorize claims if an ID becomes observable.

## Proof of Concept

The [preserved September 11 PoC log](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/contracts/audit/evidence/historical-sr01-poc.log) records:

```text
[PASS] testControl_SignedPublishForCreditsSignerEvenWhenRelayedByAttacker() (gas: 264395)
[PASS] testPoC_AttackerCanFrontRunDirectPublishAndReceiveFutureRoyalties() (gas: 311196)
```

This is retained historical output, not a fresh reproduction. It covers direct publication plus the legitimate signed-relay control; it does not show execution of the later self-signed attack variant. The report does not package the original historical PoC source or assert new build verification.

The [fixed regression source](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/test/FrontRunPublishFor.t.sol) checks outsider rejection on both routes, legitimate attester relay and signer-substitution rejection. The [September 12 fixed-suite log](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/contracts/audit/evidence/2026-09-12-hardhat-test.log) records 64 passing Solidity tests.

## Remediation

The [implemented contract fix](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/src/RecipeBook.sol) applies `onlyAttester` to both `publish` and `publishFor`, retaining author-signature verification. The attester is the crafting agent, rather than a second platform signature.

The agent's [private craft records](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/services/agent/crafted.mjs) identify permitted claimants. The [claim handlers](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/services/agent/server.mjs) reject unauthorized claims before settlement. Identical recipes can have multiple recorded crafters; registration still resolves the first permitted claim. The attester remains trusted to relay honestly. Preserve regression coverage for both contract routes and application authorization.

## Summary

SR-01 let an observer claim an unregistered ID before its creator and receive subsequent author payments. The verified fix combines contract relay restrictions with application provenance checks. [Upstream marks SR-01 closed](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/contracts/audit/SR-01-authorship-capture.md).

This portfolio entry documents Stefan's contract-audit contribution to Voxel Bench's ETHOnline 2026 project. [Upstream attribution](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/AI_USAGE.md) credits Stefan's identification and assessment of SR-01, with OpenAI Codex assisting review, tests and evidence preparation.
