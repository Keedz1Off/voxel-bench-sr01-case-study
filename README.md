# Voxel Bench SR-01: claiming someone else's recipe

**Status:** publicly acknowledged finding, fixed upstream. My documented security contribution to **ETHOnline 2026**.

- **Expected:** only an eligible crafter can register recipe authorship.
- **Original behavior:** anyone knowing an unclaimed recipe ID could register first as its author. A self-signature proved wallet control, not recipe ownership.
- **Impact:** future crafts could credit author royalties to the wrong address. Production loss was not established.
- **Fix:** trusted-attester publication plus private craft-provenance checks. The attester remains trusted.
- **Evidence:** preserved direct-path PoC, fixed regression source and a historical 64-pass Solidity suite. The self-signed variant has source/regression support, not a fresh attack execution here.

## Where to start

| Open | What you will find |
| --- | --- |
| [Matrices](#matrices) | Read the authorship rule and the trusted-attester rule. |
| [Source index](evidence/source-index.json) | Find the pinned revisions and the recorded upstream test result. |
| [GitHub Actions](#github-actions) | Check the matrix links against the saved source index. |

## Boundaries, tests and evidence

The [boundary index](matrices/boundaries.json) links the author and attester checks. The [fixed upstream regression tests](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/test/FrontRunPublishFor.t.sol) belong to the pinned Voxel Bench source. [Python tests](tests/test_recorded_evidence.py) check links in the saved evidence index.

Run the offline evidence checks from the repository root with Python 3.10 or later.

```sh
python -B -m unittest discover -s tests -v
```

## GitHub Actions

Open [Case study checks](https://github.com/Keedz1Off/voxel-bench-sr01-case-study/actions/workflows/checks.yml) and click **Run workflow**. CI reads the matrix JSON and checks the saved evidence offline. The run saves a `check-results` log. Select **CD demo** to also download `verified-delivery` with the log, commit SHA and checksum after checks pass.

### What happens in Actions

| Step | What it does |
| --- | --- |
| Checkout and Python | GitHub runs the selected commit on Ubuntu with Python 3.12. |
| Matrix JSON | CI requires the boundary index and reads every JSON file in the matrices folder. |
| Evidence tests | One test checks that the matrix points to the same historical source and fix references as the evidence index. |
| Check log | CI uploads the result as `check-results`. |
| CD demo | After a passing manual run, CI saves the log, commit SHA and SHA-256 checksum as `verified-delivery`. |

[See the workflow file](.github/workflows/checks.yml). This job checks the material shipped in this repository offline.

**Flow:** Recipe ID → authorship claim → recorded author → future royalty credits.

## Matrices

| Boundary | JSON |
| --- | --- |
| Recipe claim and wallet signature | [AUTHORSHIP](matrices/AUTHORSHIP.json) |
| Fixed trusted publication boundary | [ATTESTER](matrices/ATTESTER.json) |

Read each row as: **invariant → scenario → oracle → observation → status → evidence → limit**.

[Detailed report and source references](https://github.com/Keedz1Off/voxel-bench-sr01-case-study/tree/8ed2b57c5e51dd266fcb24844027444c86b06186) are preserved in the pinned evidence snapshot. Matrix links open the exact supporting records.

Voxel Bench SR-01; original and fixed source snapshots with historical local records. Independent, AI-assisted work. [File inventory](package-manifest.json).
