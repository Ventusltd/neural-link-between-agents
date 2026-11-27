"""Fail closed on broken or changed cross-repository evidence. Never execute remote code."""
import copy
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / ".cvaa/release-dependency-spider.json"
SHA = re.compile(r"[0-9a-f]{40}")
REPOS = {"globalgrid2050", "ventus-grid-engine", "spiders", "cvaa", "vedic-", "neural-link-between-agents"}
REQUIRED = {"golden", "spider", "genome", "spiders", "cvaa", "vedic", "readback", "neural", "protocol"}
TYPES = {"contains", "pattern_reference", "requires_read", "owner_selected_policy_reference", "proposed_ci_dependency"}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def blob_hash(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def fetch(node):
    url = "https://raw.githubusercontent.com/" + node["repo"] + "/" + node["commit"] + "/" + quote(node["path"], safe="/")
    with urlopen(Request(url, headers={"User-Agent": "CVAA-release-dependency-check"}), timeout=20) as response:
        require(response.status == 200, "dependency unavailable")
        data = response.read(2_000_001)  # source: release evidence transport budget, not engineering limit
    require(0 < len(data) <= 2_000_000, "dependency size outside evidence budget")
    return data

def validate(graph, reader):
    require(graph["schema"] == "ventus.release-dependency-spider.v1", "schema")
    require(graph["golden_url"] == "https://globalgrid2050.com/uk_renewables_pipeline/202611232245/", "golden reference changed")
    nodes = {n["id"]: n for n in graph["nodes"]}
    require(len(nodes) == len(graph["nodes"]) and REQUIRED <= nodes.keys(), "duplicate or missing node")
    cache = {}
    for ident, node in nodes.items():
        require(node["repo"] in {"Ventusltd/" + r for r in REPOS}, "unexpected repository")
        require(SHA.fullmatch(node["commit"]) and SHA.fullmatch(node["blob"]), "mutable or malformed pin")
        path = node["path"]
        require(not path.startswith("/") and all(p not in ("", ".", "..") for p in path.split("/")), "unsafe path")
        require(node["rag"] == "grey", "unsupported runtime claim")
        require(node["gh"] == "https://github.com/" + node["repo"] + "/blob/" + node["commit"] + "/" + path, "source URL mismatch")
        raw = reader(node)
        require(blob_hash(raw) == node["blob"], "blob mismatch: " + ident)
        cache[ident] = raw.decode("utf-8")
    seen = set()
    adjacency = {ident: set() for ident in nodes}
    for edge in graph["edges"]:
        key = (edge["from"], edge["to"], edge["type"])
        require(key not in seen and key[0] in nodes and key[1] in nodes and key[2] in TYPES and key[0] != key[1], "invalid or duplicate edge")
        seen.add(key)
        adjacency[key[0]].add(key[1])
        adjacency[key[1]].add(key[0])
        ev = edge["evidence"]
        require(ev["node"] in (key[0], key[1]) and bool(ev["literal"]) and ev["literal"] in cache[ev["node"]], "edge witness absent")
    pending = ["golden"]
    reached = set()
    while pending:
        ident = pending.pop()
        if ident not in reached:
            reached.add(ident)
            pending.extend(adjacency[ident] - reached)
    require(reached == set(nodes), "disconnected graph")
    return len(nodes), len(seen)

def main():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    # Fetch each immutable source once, then exercise negative cases without network.
    cache = {n["id"]: fetch(n) for n in graph["nodes"]}
    reader = lambda n: cache[n["id"]]
    n, e = validate(graph, reader)
    def reject(change):
        candidate = copy.deepcopy(graph)
        change(candidate)
        try:
            validate(candidate, reader)
        except ValueError:
            return
        raise RuntimeError("negative fixture accepted")
    reject(lambda g: g["nodes"][0].update(blob="0" * 40))
    reject(lambda g: g["nodes"][0].update(commit="main"))
    reject(lambda g: g["edges"][0].update(to="missing-node"))
    reject(lambda g: g["edges"][0]["evidence"].update(literal="absent-witness-cvaa"))
    reject(lambda g: g["edges"].append(copy.deepcopy(g["edges"][0])))
    reject(lambda g: g.update(edges=[]))
    print(json.dumps({"schema":"ventus.release-dependency-receipt.v1","status":"PASS","nodes":n,"edges":e,"negative_fixtures":6,"coverage":"all manifest nodes and declared edges; six enumerated fault injections","miss_probability":"not applicable to exhaustive declared set; unknown for undeclared dependencies","runtime_or_receiver_acceptance":False}))

if __name__ == "__main__":
    main()
