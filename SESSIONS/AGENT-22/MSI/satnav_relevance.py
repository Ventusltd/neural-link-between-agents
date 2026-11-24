#!/usr/bin/env python3
"""Read-only Stars relevance selector; optional CPU/CuPy numerical parity test.
No terrain, product edits, credentials, or live GPS. Ranking is advisory.
"""
import argparse
import hashlib
import json
import re
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

REV = "7c90d879688ca80c7ed63982eec0894fe75d67a3"
BLOB = "4b9f85af9d38bcb4173874dd095150a69282aa8b"
URL = f"https://raw.githubusercontent.com/Ventusltd/stars/{REV}/code/names.json"
GROUPS = {
    "place_search": ("queryUkGazetteer", "queryGlobalGazetteer", "geocoderGet",
                     "postcode", "gazetteer", "searchPlace", "normaliseCompact"),
    "map_selection": ("setOrigin", "mapCentre", "pickPoint", "mapClick",
                      "selectMarker", "mapPoint"),
    "destination_handoff": ("buildDestination", "parseDestination", "deepLink",
                            "setDestination", "destination"),
    "gps_compass": ("distanceKm", "initialBearingDeg", "watchPosition",
                    "geolocation", "bearing", "compass"),
}
LIMIT = 2_000_000

def read_catalogue(path):
    with (Path(path).open("rb") if path else urlopen(URL, timeout=30)) as stream:
        raw = stream.read(LIMIT + 1)
    if len(raw) > LIMIT:
        raise ValueError("catalogue exceeds byte cap")
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if blob != BLOB:
        raise ValueError(f"pinned Stars blob mismatch: {blob}")
    names = json.loads(raw)
    if not isinstance(names, dict) or not 0 < len(names) <= 100000:
        raise ValueError("catalogue shape/size invalid")
    for name, ids in names.items():
        if not isinstance(name, str) or not isinstance(ids, list) or any(
            type(i) is not int or i <= 0 for i in ids):
            raise ValueError("malformed name/family entry")
    return names, hashlib.sha256(raw).hexdigest()

def tokens(s):
    return set(re.findall(r"[a-z0-9]+", re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s).lower()))

def prepare(names):
    rows = sorted(names)
    vocab = sorted(set().union(*(tokens(q) for terms in GROUPS.values() for q in terms)))
    features = [tokens(name) for name in rows]
    queries = [set().union(*(tokens(q) for q in terms)) for terms in GROUPS.values()]
    scores = [[len(f & q) for q in queries] for f in features]
    return rows, vocab, features, queries, scores

def rank(names, rows, scores, top):
    out = {}
    for col, (group, aliases) in enumerate(GROUPS.items()):
        exact = {a.casefold() for a in aliases}
        candidates = {}
        for name, row in zip(rows, scores):
            score = row[col] + (100 if name.casefold() in exact else 0)
            if not score:
                continue
            for fid in names[name]:
                item = {"family": fid, "name": name, "score": score,
                        "source_bucket": f"https://github.com/Ventusltd/stars/blob/{REV}/code/f/{fid//500}.json"}
                old = candidates.get(fid)
                if old is None or (-score, name) < (-old["score"], old["name"]):
                    candidates[fid] = item
        out[group] = sorted(candidates.values(),
                            key=lambda x: (-x["score"], x["name"], x["family"]))[:top]
    return out

def benchmark(vocab, features, queries, reference):
    try:
        import numpy as np
        import cupy as cp
        count = cp.cuda.runtime.getDeviceCount()
        if count < 1:
            return {"status": "UNAVAILABLE", "reason": "no CUDA device"}
    except Exception as exc:
        return {"status": "UNAVAILABLE", "reason": type(exc).__name__}
    if len(features) * len(vocab) > 10_000_000:
        return {"status": "SKIPPED", "reason": "matrix exceeds cap"}
    prep = time.perf_counter()
    a = np.array([[v in row for v in vocab] for row in features], dtype=np.float32)
    b = np.array([[v in q for q in queries] for v in vocab], dtype=np.float32)
    expected = np.asarray(reference, dtype=np.float32)
    preparation_ms = (time.perf_counter() - prep) * 1000
    def gpu():
        result = cp.asnumpy(cp.asarray(a) @ cp.asarray(b))
        cp.cuda.Stream.null.synchronize()
        return result
    def measure(fn):
        t = time.perf_counter()
        result = fn()
        return result, (time.perf_counter() - t) * 1000
    first, cold = measure(gpu)
    mismatches = int(np.count_nonzero(first != expected))
    cpu_times, gpu_times = [], []
    for _ in range(3):
        c, elapsed = measure(lambda: a @ b)
        cpu_times.append(elapsed)
        g, elapsed = measure(gpu)
        gpu_times.append(elapsed)
        mismatches += int(np.count_nonzero(c != expected))
        mismatches += int(np.count_nonzero(g != expected))
    return {"status": "PASS" if not mismatches else "FAIL",
            "numpy": np.__version__, "cupy": cp.__version__,
            "device_count": count, "matrix_shape": list(a.shape),
            "preparation_ms": preparation_ms, "gpu_first_call_ms": cold,
            "cpu_median_ms": statistics.median(cpu_times),
            "gpu_transfer_inclusive_median_ms": statistics.median(gpu_times),
            "mismatch_count": mismatches, "unique_scores": int(expected.size),
            "scope": "name-token scoring only; not browser or application speedup"}

def self_test():
    names = {"queryUkGazetteer": [8307, 32867], "setOrigin": [175998],
             "initialBearingDeg": [8770], "unrelated": [1]}
    rows, _, _, _, scores = prepare(names)
    result = rank(names, rows, scores, 10)
    assert {x["family"] for x in result["place_search"]} == {8307, 32867}
    assert result["map_selection"][0]["family"] == 175998
    assert result["gps_compass"][0]["family"] == 8770
    assert not result["destination_handoff"]
    print("PASS: four deterministic relevance checks (synthetic only)")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--catalogue", help="optional local exact pinned names.json")
    p.add_argument("--out", default="satnav-relevance-receipt.json")
    p.add_argument("--gpu", action="store_true", help="optional existing CuPy environment")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return 0
    out = Path(args.out)
    if out.exists():
        p.error("output already exists; choose a new receipt path")
    receipt = {"utc": datetime.now(timezone.utc).isoformat(), "stars_commit": REV,
               "status": "FAIL", "scope": "advisory discovery, not reuse approval"}
    try:
        names, digest = read_catalogue(args.catalogue)
        start = time.perf_counter()
        rows, vocab, features, queries, scores = prepare(names)
        receipt.update(catalogue_sha256=digest, indexed_names=len(rows),
                       candidates=rank(names, rows, scores, 12),
                       cpu_selection_ms=(time.perf_counter()-start)*1000)
        receipt["gpu"] = benchmark(vocab, features, queries, scores) if args.gpu else {"status": "NOT_REQUESTED"}
        receipt["status"] = "FAIL" if receipt["gpu"]["status"] == "FAIL" else "PASS"
    except Exception as exc:
        receipt["error"] = f"{type(exc).__name__}: {exc}"
    with out.open("x", encoding="utf-8") as f:
        json.dump(receipt, f, indent=2)
        f.write("\n")
    print(f'{receipt["status"]}: {out}')
    return int(receipt["status"] != "PASS")

if __name__ == "__main__":
    raise SystemExit(main())
