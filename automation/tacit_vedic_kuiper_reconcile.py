"""Supervisor evidence reconciliation, not a runtime or source-identity allocator."""
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import quote
from urllib.request import urlopen
from zipfile import ZipFile

CONTRACT = Path(__file__).with_name("tacit_vedic_kuiper_experiment.json")
C = json.loads(CONTRACT.read_bytes())
SHA1 = re.compile(r"[0-9a-f]{40}\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
REPOS = {"Ventusltd/vedic-", "Ventusltd/ventus-grid-engine", "Ventusltd/globalgrid2050"}
LIMIT = 2_000_000

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def pin(data, expected, expected_blob=None):
    require(len(data) <= LIMIT, "SIZE")
    if expected is not None:
        require(sha(data) == expected, "SHA256")
    if expected_blob is not None:
        require(blob(data) == expected_blob, "GIT_BLOB")
    return sha(data)

def raw_url(p):
    require(p["repo"] in REPOS and SHA1.fullmatch(p["commit"]), "SOURCE_PIN")
    parts = p["path"].split("/")
    require(all(part and part not in (".", "..") for part in parts), "SOURCE_PATH")
    return ("https://raw.githubusercontent.com/" + p["repo"] + "/" +
            p["commit"] + "/" + quote(p["path"], safe="/"))

def source_list(c):
    result = {}
    for row in c["cohort"]:
        for s in row["sources"]:
            key = (s["repo"], s["commit"], s["path"], s["blob"])
            require(key not in result or result[key] == s, "CONFLICTING_SOURCE_PIN")
            result[key] = s
    return sorted(result.values(), key=lambda p: (p["repo"], p["path"]))

def acquire(directory):
    directory.mkdir(parents=True, exist_ok=True)
    items = [("dictionary.json", C["dictionary"]), ("fixture.json", C["experiment"]["fixture"])]
    items.extend((p["blob"] + ".source", p) for p in source_list(C))
    for name, p in items:
        with urlopen(raw_url(p), timeout=20) as stream:
            data = stream.read(LIMIT + 1)
        pin(data, p.get("sha256"), p.get("blob"))
        (directory / name).write_bytes(data)

def roundtrip(receipt, contract):
    """Compare fixed producer-receipt rows; not a new Kuiper resolver."""
    require(receipt["schema"] == "vedic.orient-module-receipt.v1", "RECEIPT_SCHEMA")
    require(receipt["dictionary_commit"] == contract["dictionary"]["commit"]
            and receipt["dictionary_sha256"] == contract["dictionary"]["sha256"], "EDITION")
    require(receipt["identity_complete"] is False and receipt["execution_verified"] is False,
            "UNEXPECTED_TIER_CHANGE")
    source = contract["cohort"][0]["sources"][0]
    require(all(receipt["source"].get(k) == source[k] for k in ("repo","commit","path","blob"))
            and receipt["module_sha256"] == source["sha256"], "OCCURRENCE")
    keys = {}
    ids = {}
    expected = contract["receipt"]["keys"]
    rows = receipt["components"]
    require(len(rows) == len(expected), "COMPONENT_COUNT")
    for row in rows:
        mid = row["gg_id"]
        key = row["kuiper"]["key"]
        require(type(key) is int and key > 0, "KEY_TYPE")
        require(mid not in ids and key not in keys, "DUPLICATE_JOIN")
        require(row["kuiper"]["state"] == contract["receipt"]["tier"], "KEY_TIER")
        require(all(row["source"].get(k) == source[k] for k in ("repo","commit","path","blob")),
                "COMPONENT_OCCURRENCE")
        ids[mid] = key
        keys[key] = mid
    for p in expected:
        require(ids.get(p["meaning"]) == p["key"] and keys.get(p["key"]) == p["meaning"],
                "KEY_ROUNDTRIP")
        require(next(r for r in rows if r["gg_id"] == p["meaning"])["export"] == p["export"],
                "EXPORT")
    require(keys.get(-1) is None, "UNKNOWN_KEY")
    return [{"meaning":mid,"key":key,"state":contract["receipt"]["tier"]}
            for mid,key in sorted(ids.items())]

def validate_cohort(c, dictionary):
    entries = dictionary["entries"]
    ids = {e["gg_id"] for e in entries}
    require(len(ids) == len(entries), "DUPLICATE_MEANING")
    require(len(c["cohort"]) == 4 and {r["family"] for r in c["cohort"]} ==
            {"orient","electrical","nearest","solar"}, "COHORT")
    for row in c["cohort"]:
        require(set(row["meanings"]) <= ids, "UNKNOWN_MEANING")
        require(row["review"] == "PENDING" and row["rights"] == "BLOCKED"
                and row["publication"] == "NOT_PUBLISHED", "UNSUPPORTED_PROMOTION")
        if row["family"] != "orient":
            require(row["admission"] != "ADMITTED_INTERNAL", "UNSUPPORTED_ADMISSION")
            require(row["evidence"]["archive_kind"] != "SHARED_FACTORY_INTERNAL",
                    "UNSUPPORTED_ARCHIVE")
    return len(ids)

def fixture_reference(f, contract):
    """Independent fixture expectation, not invocation of the producer."""
    require(f["provenance"] == "synthetic", "FIXTURE_PROVENANCE")
    inputs = f["input"]
    require(inputs["crs"] == "EPSG:4326" and inputs["minimumKv"] == 132, "INPUT_CONTRACT")
    require(inputs["query"] == {"longitude":0,"latitude":0}, "ORIGIN")
    records = inputs["records"]
    require(len({r["id"] for r in records}) == len(records), "DUPLICATE_ID")
    require(all(r["location"]["latitude"] == 0 and 0 < r["location"]["longitude"] < 180
                for r in records), "EQUATORIAL_FIXTURE_ONLY")
    eligible = [r for r in records if any(v >= inputs["minimumKv"] for v in r["voltages_kv"])]
    require(bool(eligible), "NO_ELIGIBLE_RECORD")
    selected = min(eligible, key=lambda r: r["location"]["longitude"])
    # For this eastward equatorial fixture, arc length = radius * angle.
    km = 6378.137 * math.radians(selected["location"]["longitude"])
    expected = contract["experiment"]["expected"]
    require(selected["id"] == expected["id"] == f["expected"]["id"], "SELECTED_ID")
    require(abs(km-expected["distance_km"]) <= expected["tolerance_km"]
            and abs(km-f["expected"]["distance_km"]) <= expected["tolerance_km"], "DISTANCE")
    require(expected["bearing_deg"] == 90, "BEARING")
    require(contract["experiment"]["state"] == "COMPOSITION_BLOCKED_PENDING_NEAREST_ADMISSION",
            "UNSUPPORTED_COMPOSITION")
    return {"selected_id":selected["id"],"distance_km":km,"bearing_deg":90,
            "state":"REFERENCE_EXPECTATION_ONLY_NOT_PRODUCER_EXECUTION"}

def property_check(p):
    require(set(p) == set(C["property_contract"]["fields"]), "PROPERTY_FIELDS")
    require(p["state"] in C["property_contract"]["allowed_states"], "PROPERTY_STATE")
    require((p["value"] is None and bool(p["unknown_reason"])) if p["state"] == "UNKNOWN"
            else (p["value"] is not None and p["unknown_reason"] is None), "UNKNOWN_RULE")
    require(bool(p["source_occurrence"]) and bool(p["definition_version"]) and bool(p["method"])
            and SHA256.fullmatch(p["input_sha256"]), "PROPERTY_PROVENANCE")
    require(bool(p["evidence_ref"]), "PROPERTY_EVIDENCE")

def reconcile(directory):
    raw = (directory/"dictionary.json").read_bytes()
    pin(raw,C["dictionary"]["sha256"])
    count = validate_cohort(C,json.loads(raw))
    actual = []
    for p in source_list(C):
        data = (directory/(p["blob"]+".source")).read_bytes()
        digest = pin(data,p.get("sha256"),p["blob"])
        actual.append({**p,"observed_sha256":digest,"bytes":len(data)})
    with ZipFile(directory/"receipt.zip") as z:
        name = C["receipt"]["path"]
        require(z.namelist().count(name) == 1 and z.getinfo(name).file_size <= LIMIT, "RECEIPT_ZIP")
        raw_receipt = z.read(name)
    pin(raw_receipt,C["receipt"]["sha256"])
    keys = roundtrip(json.loads(raw_receipt),C)
    fixture = (directory/"fixture.json").read_bytes()
    reference = fixture_reference(json.loads(fixture),C)
    # Explicitly unknown example for schema validation only, not producer property evidence.
    property_check(dict(source_occurrence=C["cohort"][0]["sources"][0],
                        property="runtime_cost",definition_version="candidate.v1",
                        value=None,unit="ms",method="not measured",
                        input_sha256=C["cohort"][0]["sources"][0]["sha256"],
                        evidence_ref="contract-only",state="UNKNOWN",unknown_reason="no benchmark"))
    return {"schema":"tacit.vedic-kuiper-supervisor-reconciliation.v1",
            "contract_sha256":sha(CONTRACT.read_bytes()),"dictionary_entries":count,
            "verified_source_occurrences":actual,"producer_receipt_joins":keys,
            "fixture_sha256":sha(fixture),"fixture_reference":reference,
            "cohort":C["cohort"],"independent_acceptance":False,
            "composition_executed":False,"publication_authorized":False}

class Contracts(unittest.TestCase):
    def test_hash(self):
        with self.assertRaisesRegex(ValueError,"SHA256"): pin(b"wrong","0"*64)
    def test_blob(self):
        with self.assertRaisesRegex(ValueError,"GIT_BLOB"): pin(b"wrong",None,"0"*40)
    def test_fixed_url(self):
        with self.assertRaisesRegex(ValueError,"SOURCE_PIN"):
            raw_url(dict(repo="other/repo",commit="a"*40,path="a"))
    def test_path(self):
        with self.assertRaisesRegex(ValueError,"SOURCE_PATH"):
            raw_url(dict(repo="Ventusltd/vedic-",commit="a"*40,path="../a"))
    def test_promotion(self):
        c=copy.deepcopy(C)
        c["cohort"][1]["admission"]="ADMITTED_INTERNAL"
        d={"entries":[{"gg_id":m} for m in sorted({m for r in c["cohort"] for m in r["meanings"]})]}
        with self.assertRaisesRegex(ValueError,"UNSUPPORTED_ADMISSION"): validate_cohort(c,d)
    def test_unknown_property(self):
        p=dict(source_occurrence={"candidate":"synthetic"},property="test",definition_version="v1",
               value=0,unit="ms",method="none",input_sha256="a"*64,evidence_ref="fixture",
               state="UNKNOWN",unknown_reason="not observed")
        with self.assertRaisesRegex(ValueError,"UNKNOWN_RULE"): property_check(p)
    def test_wrong_occurrence(self):
        s=C["cohort"][0]["sources"][0]
        r=dict(schema="vedic.orient-module-receipt.v1",dictionary_commit=C["dictionary"]["commit"],
               dictionary_sha256=C["dictionary"]["sha256"],identity_complete=False,
               execution_verified=False,source={**s,"commit":"a"*40},module_sha256=s["sha256"])
        with self.assertRaisesRegex(ValueError,"OCCURRENCE"): roundtrip(r,C)
    def test_duplicate_key(self):
        s=C["cohort"][0]["sources"][0]
        r=dict(schema="vedic.orient-module-receipt.v1",dictionary_commit=C["dictionary"]["commit"],
               dictionary_sha256=C["dictionary"]["sha256"],identity_complete=False,
               execution_verified=False,source=s,module_sha256=s["sha256"],
               components=[dict(gg_id="GG2050-VEDIC-000001",source=s,kuiper={"key":1,"state":C["receipt"]["tier"]})]*2)
        with self.assertRaisesRegex(ValueError,"DUPLICATE_JOIN"): roundtrip(r,C)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--acquire",type=Path)
    p.add_argument("--reconcile",type=Path)
    args=p.parse_args()
    if args.self_test:
        unittest.main(argv=[sys.argv[0]])
    elif args.acquire:
        acquire(args.acquire)
    elif args.reconcile:
        print(json.dumps(reconcile(args.reconcile),sort_keys=True,indent=2))
    else:
        p.error("choose an operation")

if __name__ == "__main__":
    main()
