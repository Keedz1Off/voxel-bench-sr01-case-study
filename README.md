# Voxel Bench SR-01: claiming someone else's recipe

**Status:** publicly acknowledged finding, fixed upstream. My documented security contribution to **ETHOnline 2026**.

- **Expected:** only an eligible crafter can register recipe authorship.
- **Original behavior:** anyone knowing an unclaimed recipe ID could register first as its author. A self-signature proved wallet control, not recipe ownership.
- **Impact:** future crafts could credit author royalties to the wrong address. Production loss was not established.
- **Fix:** trusted-attester publication plus private craft-provenance checks. The attester remains trusted.
- **Evidence:** preserved direct-path PoC, fixed regression source and a historical 64-pass Solidity suite. The self-signed variant has source/regression support, not a fresh attack execution here.

**Flow:** Recipe ID → authorship claim → recorded author → future royalty credits.

## Matrices

| Boundary | JSON |
| --- | --- |
| Recipe claim and wallet signature | [AUTHORSHIP](matrices/AUTHORSHIP.json) |
| Fixed trusted publication boundary | [ATTESTER](matrices/ATTESTER.json) |

Read each row as: **invariant → scenario → oracle → observation → status → evidence → limit**.

[Detailed report, tests, logs and source pins](https://github.com/Keedz1Off/voxel-bench-sr01-case-study/tree/8ed2b57c5e51dd266fcb24844027444c86b06186) are preserved in the pinned evidence snapshot. Matrix links open the exact supporting records.

Voxel Bench SR-01; original and fixed source snapshots with historical local records. Independent, AI-assisted work. Documentation reorganisation only; no new target tests. [File inventory](package-manifest.json).
