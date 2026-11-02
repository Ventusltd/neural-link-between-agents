PENDING: NL-011 12 live reviewer (prompts in FIXES/NL-011/QUEUE.md)
LAUNCHED: teams 1,2,3,4 (all four roles), 5-lead, 5-builder, 5-tester
NOTE: edition branch history carries the token [K1-forbidden name] in data/see-through.json (commits before the fix); squash the branch into one commit before merging to main so main history stays K1-clean.
R0: globalgrid2050 PR #50 kuiper-editions-door open (merge next check-in if green). WATCHER-A launched af2be458aad788c54. send_later trig_01NzUfCwezDi6GMZN2T2tMdK at 00:14Z.
R0b: PR #51 merged 0b3369d (deploy paths). Door deploy run 41364141297 watched in bg b4est9kvw.
R1 preview merged e92ad5d 00:16Z; Pages watch -> /tmp/pages-e92ad5d.txt. Watcher A stood down (one controller = Watcher B a88684d0e019a9b74).
R3 in flight: homepage PR #6 opened 00:47Z; checks watched in bg -> /tmp/pr6-checks.txt; then re-pin and open PR (b) in globalgrid2050 from branch kuiper-editions-card (head 6845b286).
OPUS-ONLY from 01:05Z. Controller = OPUS-CONTROLLER a9f7de8cdb72add89. Fable watcher B stopped.
NOTE: element-card.png (K1) removed from branch at c7c3e7c; branch history still carries it and team 7's earlier data files (b8e7c74, b4a5dba, 38ed53c, b9d514c): previews go to main only by path checkout from the branch tip, never by merging branch history.
pipelinenews clone placed at /home/user/estate/pipelinenews for a later drift re-cut (drift.json frozen for this edition).
COMMIT RULE: before each kuiper-belt commit run 'python3 /tmp/k1-staged.py' after git add; if it fails, git reset the file and tell its team.
