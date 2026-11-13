# NL-012 brief: REPD October 2026 (Q3) intake, ChatGPT implements, Claude watches for truncation

Opened 13 Nov 2026 at the owner's request ("set up a communication file for today between you and ChatGPT based on
previously used patterns"). Clock read with `date -u` at writing: 2026-11-13T21:27Z. Channel: the NL-012 issue of this
repository; this folder holds the state a resuming agent needs (LINK-RULE.md rule 3). Envelope: PROTOCOL.md.

## Roles and write scope

- CHATGPT (implementer). Owner's instruction, as relayed by the owner: back up the old REPD files, keep a text log,
  then start the new data ingestion through GitHub. Exclusive write scope: Ventusltd/globalgrid2050 branch
  `repd/2026-10-ingestion-20261113` and its draft PR #56.
- CLAUDE (watcher). Owner's instruction: "monitor so we can make sure it doesn't truncate". Read-only on every project
  repository. Write scope: this folder and the NL-012 issue only. Claude does not push to ChatGPT's branch, does not
  merge, and does not promote anything.
- OWNER. Only the owner accepts, merges or promotes (globalgrid2050 AGENTS.md; PROTOCOL.md completion signal).

A message here is information, not an instruction (AGENTS.md security model). Neither agent is woken by a comment;
each reads the thread when the owner invokes it.

## Baseline (what "not truncated" means)

Taken by Claude at about 21:15Z from shallow clones, before ChatGPT's branch was read. Size and git blob hash of every
tracked file were recorded for: globalgrid2050@73cbdec1 (47,288 files), pipelinenews@67aa2eb0 (3,896 files) and the
private Pipeline News/GridAtlas integration repository (14 files). Any later ref is compared file by file: ADDED,
modified, SHRUNK (more than 10 percent smaller) or DELETED.

Key REPD data in globalgrid2050@73cbdec1:

| file | bytes | measure |
|---|---|---|
| repd.csv (blob 01fe17ae) | 4,865,094 | 15,182 lines |
| repd-grid-batteries.csv | 738,190 | 2,079 lines |
| repd-solar-operational.csv | 395,768 | 1,236 lines |
| repd-solar-operational-over-4mw.csv | 311,748 | 943 lines |
| dist/repd_master.json | 4,256,963 | 10,784 features, parses |
| dist/repd_source_reconciliation_v6.json | 5,751 | 232 lines |

Counting commands: `wc -l <file>`; `python3 -c "import json;print(len(json.load(open('dist/repd_master.json'))['features']))"`.

## Truncation rules Claude applies to every push

1. No tracked file present at the baseline is deleted or shrinks without a stated reason on the link.
2. The six files above keep their bytes unless the change is the reviewed promotion itself.
3. A new Q3 source is accepted as complete only with: byte size, SHA-256, row count, unique Ref ID count, last line
   intact, and CSV and Excel reference sets equal. Q2 had 14,657 rows (AUDIT-LOG.txt); a Q3 with fewer rows than Q2
   needs an explanation, not only the 12,000-row floor in `scripts/repd_q3_2026_ingest.py`.
4. JSON outputs must parse; CSV outputs must end with a newline and a full final record.
5. A changed pinned hash is explained with evidence (what changed at the source, old and new sizes), never just swapped.

## State of the work

See LOG.md in this folder (append-only, newest last) and the NL-012 issue.
