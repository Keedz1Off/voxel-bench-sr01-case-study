# SR-01: before and after

## Original path

```mermaid
sequenceDiagram
    participant A as Alice: legitimate creator
    participant M as Mallory: observer
    participant B as RecipeBook
    participant V as SplitVault
    Note over A,M: Alice's recipe ID becomes visible before registration
    M->>B: publish(ID), using Mallory's own wallet
    B->>B: Record Mallory as author
    A->>B: Claim the same ID
    B-->>A: AlreadyPublished
    Note over B,V: A later paid craft credits the recorded author
    B->>V: Credit Mallory's author share
```

The preserved original PoC log covers this direct-publication attack plus a legitimate signed-relay control. Source inspection also establishes why Mallory's own valid signature could satisfy the original `publishFor` checks; that variant is not claimed as an execution in the same historical PoC log.

## Implemented fix

```mermaid
flowchart TD
    C["Claim: recipe ID, author, signature"] --> A["Agent checks recorded permitted crafters"]
    A -->|not permitted| N["Refuse before settlement"]
    A -->|permitted| R["Attester relays claim"]
    R --> B["RecipeBook checks onlyAttester"]
    B --> S["Verify author signature"]
    S --> O["Record author if ID is unclaimed"]
```

The contract gates **both** `publish` and `publishFor`. The signed route additionally checks the author signature. The attester must accurately enforce provenance: the contract alone cannot determine who crafted the content. Identical recipes may have more than one permitted crafter; the first permitted registration wins.

This is an authorization/provenance issue, not broken EIP-712 cryptography. Test coverage is not a claim that every web, payment, identity or deployment path was audited.

Read [CASE-STUDY.md](CASE-STUDY.md) for exact source snapshots, prerequisites and evidence limits.
