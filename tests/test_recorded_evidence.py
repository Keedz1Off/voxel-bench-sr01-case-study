"""Offline checks of the evidence shipped with this portfolio entry."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class RecordedEvidenceTests(unittest.TestCase):
    def test_current_matrix_links_to_the_same_historical_sources(self):
        source = read_json("evidence/source-index.json")
        rows = read_json("matrices/boundaries.json")["rows"]
        urls = {entry["url"] for row in rows for entry in row["evidence"]}
        original = "contracts/audit/evidence/historical-sr01-poc.log"
        fixed = "contracts/audit/evidence/2026-09-12-hardhat-test.log"
        self.assertIn(source["evidence"][original]["url"], urls)
        self.assertIn(source["evidence"][fixed]["url"], urls)
        self.assertFalse(source["validation"]["newTargetTests"])
