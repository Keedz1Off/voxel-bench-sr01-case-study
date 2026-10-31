# How to read this case

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Short explanation, contribution and status. |
| [FLOW.md](FLOW.md) | Original capture and implemented authorization boundary. |
| [CASE-STUDY.md](CASE-STUDY.md) | Source-backed report, impact, fix and historical validation. |
| [SOURCES.json](SOURCES.json) | Immutable source/evidence links and validation scope. |

## Check the evidence

- [Vulnerable RecipeBook](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/5015954e807783a9d6e68cff07984ce98556cfa0/contracts/src/RecipeBook.sol): follow `publish`, `publishFor`, `_publish`, then `craft`.
- [Historical PoC log](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/contracts/audit/evidence/historical-sr01-poc.log): successful direct-publication capture and legitimate signed-relay control.
- [Fixed contract](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/src/RecipeBook.sol): both publication routes require `onlyAttester`.
- [Fixed regression test](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/test/FrontRunPublishFor.t.sol): outsider rejection, legitimate relay and explicit attester trust.
- [Application claim gate](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/services/agent/server.mjs) and [craft records](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/services/agent/crafted.mjs): eligibility is checked before settlement.
- [Historical fixed-suite log](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/contracts/audit/evidence/2026-09-12-hardhat-test.log): 64 passing Solidity tests, not a new run performed for this portfolio update.
- [Project attribution](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/AI_USAGE.md): Stefan's audit contribution and AI assistance.

Read the code and actual run records before interpreting the count of passing tests. An older upstream attack-trace document contains a superseded platform-signature sketch; this case follows the implemented attester-relay design.
