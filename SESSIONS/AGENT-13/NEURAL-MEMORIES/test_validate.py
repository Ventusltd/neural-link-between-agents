import copy
import json
from pathlib import Path
import unittest

from validate import unique, validate


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(Path(__file__).with_name("20261116-build-ledger.json").read_text(encoding="utf-8"))

    def reject(self, edit, message):
        edit(self.doc)
        with self.assertRaisesRegex(ValueError, message):
            validate(self.doc)

    def test_actual_handoff_has_ordered_dependencies_and_no_public_claim(self):
        result = validate(self.doc)
        self.assertEqual(result["public_pipeline_count"], 0)
        order = result["code_dependency_order"]
        self.assertLess(order.index("figures"), order.index("covenant_ledger"))
        self.assertLess(order.index("prospecting_ui"), order.index("prospecting_export"))

    def test_missing_dependency(self):
        self.reject(lambda d: d["components"][0]["code_requires"].append("absent"), "missing dependency")

    def test_cycle(self):
        self.reject(lambda d: d["components"][0]["code_requires"].append("news_consumer"), "dependency cycle")

    def test_stale_ci_does_not_follow_new_head(self):
        self.passing_candidate_ci()
        self.reject(lambda d: d["milestones"][0].update(head="f" * 40), "stale CI head")

    def test_count_cannot_be_incremented_without_publication(self):
        self.reject(lambda d: d.update(public_pipeline_count=1), "count differs")

    def test_passing_ci_alone_is_not_publication(self):
        self.passing_candidate_ci()
        self.reject(lambda d: d["milestones"][0].update(published=True), "public receipt")

    def passing_candidate_ci(self):
        row = self.doc["milestones"][0]
        row["ci"] = {
            "status": "observed_pass",
            "tested_head": row["head"],
            "urls": ["https://github.com/example/repository/actions/runs/1"],
        }

    def test_release_dependency_missing(self):
        self.reject(lambda d: d["milestones"][1]["requires_release"].append("V0"), "missing dependency")

    def test_machine_verification_rejected(self):
        self.reject(lambda d: d["invariants"].update(automatic_verified=True), "machine verification")

    def test_old_version_delta_cannot_be_blind_cherry_pick(self):
        def edit(d):
            row = next(c for c in d["components"] if c["id"] == "dc_expansion")
            row["next_action"]["command"] = "git cherry-pick " + row["authored_commits"][0]
        self.reject(edit, "historical-path")

    def test_duplicate_inventory_key(self):
        self.reject(lambda d: d["components"].append(copy.deepcopy(d["components"][0])), "duplicate id")

    def test_short_commit_is_not_exact_pin(self):
        self.reject(lambda d: d["components"][0]["authored_commits"].__setitem__(0, "c2b89326"), "invalid source commit")

    def test_private_path_is_not_public_memory(self):
        self.reject(lambda d: d["coverage"]["missing"].append("C:/Users/example/private"), "private path")

    def test_json_duplicate_keys_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            json.loads('{"status": "PASS", "status": "FAIL"}', object_pairs_hook=unique)


if __name__ == "__main__":
    unittest.main()
