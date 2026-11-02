# Voxel Bench SR-01: claiming someone else's recipe

**Status:** publicly acknowledged finding, fixed upstream. My documented security contribution to **ETHOnline 2026**.

- **Expected:** only an eligible crafter can register recipe authorship.
- **Original behavior:** anyone knowing an unclaimed recipe ID could register first as its author. A self-signature proved wallet control, not recipe ownership.
- **Impact:** future crafts could credit author royalties to the wrong address. Production loss was not established.
- **Fix:** trusted-attester publication plus private craft-provenance checks. The attester remains trusted.
- **Evidence:** preserved direct-path PoC, fixed regression source and a historical 64-pass Solidity suite. The self-signed variant has source/regression support, not a fresh attack execution here.

## Evidence and details

[Boundary matrix](matrices/boundaries.json) · [Flow](FLOW.md) · [Case study](CASE-STUDY.md) · [Pinned sources](SOURCES.json)

[Upstream acknowledgement](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/2734fc4e31a6763986a62d5bdf2704e770c1c71d/docs/CONTRACT_AUDIT.md#findings) · [Implemented fix](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/commit/ba067ec240835cbc9e03bb991e644b75a1f30eb6) · [File map](READING-GUIDE.md) · [Web3 portfolio](https://github.com/Keedz1Off/web3-security-portfolio).

Historical local evidence and AI-assisted source review; no new target execution in this edit.
