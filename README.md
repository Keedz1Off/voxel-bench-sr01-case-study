# Voxel Bench recipe authorship

My security contribution to **ETHOnline 2026** was a publicly acknowledged finding in recipe authorship. The team shipped a fix that requires a trusted attester to confirm eligibility before recipe publication.

Incorrect authorship could affect future royalty attribution. A retained upstream record reports **64 passing Solidity tests** for the fix. The current workflow checks the portfolio evidence index against the pinned source references.

## Evidence

- [Recorded source and fix references](evidence/source-index.json) · [Boundary matrix index](matrices/boundaries.json)
- [Authorship rules](matrices/AUTHORSHIP.json) · [Attester rules](matrices/ATTESTER.json)
- [Upstream regression tests](https://github.com/ETH-GLOBAL-ONLINE/voxel-bench/blob/ba067ec240835cbc9e03bb991e644b75a1f30eb6/contracts/test/FrontRunPublishFor.t.sol)

## Run the checks

[Open Case study checks in GitHub Actions](https://github.com/Keedz1Off/voxel-bench-sr01-case-study/actions/workflows/checks.yml) and select **Run workflow**. CI runs one offline test that checks the saved matrix and source references.

The run saves `check-results`. Select **CD demo** to also package the passing log, commit SHA and checksum as `verified-delivery`.

Run locally with Python 3.10 or later:

```sh
python -B -m unittest discover -s tests -v
```
