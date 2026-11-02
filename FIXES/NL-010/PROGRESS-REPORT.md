# NL-010 progress report for the owner (2 November 2026)

Written by FABLE-FIN-3 for Vikram Kumar, Ventus Ltd. DRAFT, clock read with `date -u` at 10:31 UTC on 2 November
2026; the final version folds in FABLE-FIN-1's FINDING and FABLE-FIN-2's REVIEW on issue #10. Every number here
carries a key in brackets. A key of the form `#10/c6567194090` is a comment on
https://github.com/Ventusltd/neural-link-between-agents/issues/10 (comment id after `c`); a key of the form
`OVERNIGHT.md:53` is a line of a file in this repository, and FIXES/NL-011/KUIPER-MAP.md gives the commit that wrote
that line (`nl@<commit> path:line`); `kb@<sha>` is a kuiper-belt commit; `run <id>` is a GitHub Actions run.

## 1. What is live now, and where

The editions pointer https://ventusltd.github.io/kuiper-belt/editions/ opens Kuiper Edition 11. The door
www.globalgrid2050.com/kuiper-editions/ forwards to that pointer, and the homepage's Kuiper editions card opens the
door; the homepage's See Through entry opens the See Through pointer, which opens See Through 202611020012. Nothing
was deleted: Editions 1 to 10 and See Through 202610050609 stay as history. (kb@94aa593; #10/c6574744989;
#10/c6566414726; #10/c6567739175)

Seven editions were published between 01:47 and 10:22 UTC, each a new dated folder, each one module on the last:

- Edition 5, stamp 202611012135. Edition 4's wafer with the NL-009 Android fixes, a hook table and a loader that admits
  stamped modules by sha256 and refuses in words, and the card law (every card opens with the line of code itself, the
  key second). Shipped kb@a432b43 at 01:47 UTC, corrected at kb@521dca75 at 02:55 UTC (section 2). Green state G2:
  hello + line-card, Pixel 7 14/16 and Galaxy S24 14/16, the two reds being the base's own (bar on two rows, no See
  Through control). Verified on both phones at 521dca75: 16/18 each, no new red. (#10/c6567194090; #10/c6567953002;
  #10/c6568615624)
- Edition 6, 202611020326. The GridAtlas bar: FILE EDIT VIEW · VENTUS · SCOPE WAFER ABOUT in one 34 px row, the Ventus
  wordmark, See Through as a bar title from 434 px and a bottom-left strip below it (shell rev 3, 2045c51a).
  kb@8cb2235, 03:29 UTC, Pages run 41383399289. Shell journey Galaxy S24 16/16, Pixel 7 15/16 (a screenshot timeout,
  not the shell). Independent verify: 16/16 on both phones, the two base reds now green. (#10/c6568373074;
  #10/c6568299280; #10/c6568998242)
- Edition 7, 202611020446. The line card's landscape revision (8ec117f9): on a landscape phone the card no longer
  fills before its details open. kb@4ee309d, 04:47 UTC, from GREEN row E6-G1 at branch commit 84f1c1ed; Pixel 7
  16/16, Galaxy S24 16/16. (#10/c6569312507; #10/c6568897062)
- Edition 8, 202611020528. The drift (f03b7835): is every quoted line still at the head of its repository? At the
  cut: 346 lines, 309 SAME, 7 MOVED, 2 GONE, 0 FILE_GONE, 28 UNVERIFIED. kb@87031c6, 05:30 UTC, from E6-G2 at
  553e58d7; 16/16 and 16/16; the drift's own test 57/57 on both phones. (#10/c6569860419; #10/c6568883224)
- Edition 9, 202611020629. The app launcher (fa01e012): FILE › Open an app lists 34 apps of the estate, See Through
  first, one 44 px row each, the key as the row's header. kb@fdf6e35, 06:31 UTC, from E6-G3 at b553b1f1; 16/16 and
  16/16; the launcher's own test 12/12 script gates and 17/17 device gates on both phones. (#10/c6570717660;
  #10/c6570675769)
- Edition 10, 202611020825. The layers registry (c8fccccf): seven layers switched on and off as GridAtlas does;
  periods, repositories, editions, verified lines (344 of 346), spider graphs OK; See Through stars EMPTY; periodic
  table REFUSED until the elements licence is settled. kb@35ef064, 08:28 UTC, from E9-G1 at 85c0bc64 by an independent
  controller; 16/16 and 16/16 on base and on base plus layers. (#10/c6572568222; #10/c6572503742)
- Edition 11, 202611021017. The GridAtlas File menu (5fc4e307): open a key, open a line, open an app, and the
  edition's evidence, seven files measured live when FILE opens. kb@94aa593, 10:22 UTC, from E10-G1 at 977de9c2;
  16/16 and 16/16 on base and base plus File; by touch on Pixel 7 FILE's smallest target is 44 px and Open a key
  opens the card. (#10/c6574744989; #10/c6574630072)

See Through 202611020012 (kb@7110022, 02:14 UTC, Pages run 41376685032) reads the Kuiper's deep links (#sub, #key with
or without &space, #repo, #view) and gives every star a row that opens it on the Kuiper. Tester PASS 23/23 on Pixel 7
on the shipped bytes; Galaxy S24 was not run; #repo lights amber not cyan; the line-of-code note clips at 404 px on a
412 px phone. The See Through pointer moved to it in its three places. (#10/c6567465379; #10/c6567437030;
#10/c6567478191)

The www.globalgrid2050.com side: the door /kuiper-editions/ (globalgrid2050 PR #50, merged 23:38 UTC on 1 Nov,
deploy run 41364141297); the deploy allow-list line (PR #51, 23:58 UTC); the Kuiper editions homepage card
(globalgrid2050-homepage PR #6 and globalgrid2050 PR #52, deploy run 41368222618 success at 00:38 UTC); the See
Through entry pointing at the stable pointer (homepage PR #7 and globalgrid2050 PR #53, restore point v137, deploy
run 41378168206 success at 02:31 UTC). (OVERNIGHT.md:39; OVERNIGHT.md:45; #10/c6567739175)

## 2. The release process that worked

From Edition 6 on, a release had four parts. An independent Opus controller admits one module at a time into a
frozen snapshot of the shipped edition, runs the sixteen-step Android journey on Pixel 7 and then on Galaxy S24, and
writes a GREEN row only when no step turned red on either phone. The GREEN row names the branch commit whose folder
bytes were journeyed, with the sha256 of index.html and modules.json. The harness checks out that named commit, checks
those two sha256 values against the row, copies the folder to a new dated stamp, moves the pointer in its three
places, runs ci_check (K1, 0 leaks every time) and a render check on both phones, merges to main, and watches the Pages
run. Each step is one comment on #10 with the run id. (editions/202611020326/GREEN.md on the edition branch;
#10/c6568437190; #10/c6567953002)

The rule that the harness checks out a named commit came from the one incident of the night. Edition 5 shipped at
01:47 UTC with modules.json 4e6b4031 (hello, line-card, see-through) instead of the green manifest be99c8a1 (hello,
line-card): the controller admitted see-through at 01:49 between the harness reading the order and checking out the
folder, and the team 9 tester measured card-details red on both phones on the shipped bytes. The wrong state was live
from about 01:52 to 03:00 UTC. kb@521dca75 restored the green manifest and cut proof/edition-sha256.txt over all 188
files. Rule from then on: a release reads a named commit's manifest and verifies its sha256 against the GREEN row
before merging; it never reads the branch's live working tree. (OVERNIGHT.md:53; #10/c6567874903; #10/c6567953002)

Two harness rulings shaped the green rows: a whole-wafer step whose only failure is the 180 s screenshot timing out,
with every page condition met and the step's own frame measuring a whole wafer (ratio at least 0.95), counts as
HARNESS-LIMITED PASS; and card-details passes at the card's height cap when the details are reachable inside the
card. (#10/c6568437190; #10/c6568562808)

One admission was an exception to the tester rule: the line card revision 8ec117f9 was admitted on the OPUS-2 lead's
own 24/24 run under the harness's written instruction, because no team 2 tester run existed; it then measured 16/16
on both phones in the controller's journey. (editions/202611020326/GREEN.md note E6-G1; #10/c6568562808)

## 3. The ten-step roadmap, step by step

The roadmap (ROADMAP.md, consolidated 21:34 UTC on 1 Nov, #10/c6564201811) set ten steps. Their state at 10:31 UTC:

1. The shell contract (GridAtlas bar, Ventus wordmark, six menus): shipped in Edition 6 (rev 3). Q7, the See Through
   slot on a phone, waits on the owner (section 6).
2. The card law (the line of code is the header): shipped in Edition 5; the landscape revision in Edition 7. The
   LAWS.md L11 patch is written in handoff/02-card and not yet applied to kuiper-belt's LAWS.md (it was to ride in
   PR B, which the delegation replaced). (LEDGER.md row 02-card/REQUESTS.md:11)
3. The layer registry: shipped in Edition 10, after a first revision was refused at 04:24 UTC (a spark tap opened the
   wrong card). (#10/c6569024455; #10/c6572503742)
4. The cartridge law (hook table, loader, manifest, refusal in words): shipped in Edition 5. edition_check E1–E9 exists
   on the edition branch; E3, E6 and E7 fail for known reasons (section 7).
5. See Through, the star player: half shipped. See Through 202611020012 with the deep-link reader is live and linked
   from the homepage, and the shell carries the SEE THROUGH entry (title or strip). The Kuiper-side module (the 5,800
   See Through stars as a layer, the card's "see this line among the stars") was refused by its tester and has no
   revision yet; the layers row reads EMPTY. (#10/c6567342104; #10/c6570675769; #10/c6574744989)
6. The File menu and the hash grammar: shipped in Edition 11, with thinner evidence than its first draft (section 7).
7. The OS baby step (app registry, launcher, periodic table, spider): the launcher and registry shipped in Edition 9.
   The periodic-table layer is REFUSED until Q1 is answered; the spider graphs are copied as DISCLOSED pending Q5.
8. The drift: shipped in Edition 8.
9. The release law and licence register: edition_check E1–E9, editions/LAW.md and LICENCES.md were delivered by team 9
   on the branch; check.yml on main runs ci_check only; the branch's own check ("Check the editions by their law")
   has been red since 03:20 UTC on the stray and pre-cut files (run 41427484228). The owner-ACCEPT step of 9.6 was
   suspended by the overnight delegation. (#10/c6567128344; #10/c6566796733)
10. The Opus plan: executed as written for the module teams; the PR A / PR B route was replaced by path-checkout
    releases from GREEN rows under the delegation. (#10/c6566796733; #10/c6567437030)

Phase 2 (per-app Kuipers, the Kuiper that counts everything, the unique-lines Kuiper) is gated on the owner's
acceptance of steps 1–10 and nothing of it has been built. (ROADMAP.md:784)

## 4. The neural link as a medium

What worked: the link is a good record. 131 of 139 envelopes were complete; 200 of 201 sha256 values posted equalled
real bytes and none was invented; every refusal named a hash, a count or a measurement; wherever a seal existed it
caught the problem (the loader refused a shell edited after hand-off; the controller restored an overwritten loader by
hash; the team 9 tester caught the wrong Edition 5 manifest from the served bytes). Since the owner's rule of 01:13 UTC
(LINK-RULE.md) the harness's rulings, delegations and each release went on the link within minutes, and a resume kit,
an index, a decision log and a ledger let a new session start from the repository alone. (SYNTHESIS.md; LINK-RULE.md:1;
RESUME.md:1; INDEX.md:1; DECISIONS.md:1; LEDGER.md:1)

What did not: it was not a channel. Zero ACKs on #10; 3 of 27 directed comments answered by comment id; 18 asks open
at 01:05; content travelled through hand-off files (about 7.6 file touches per issue touch) and attention through
harness direct messages. About 754 agent-minutes went on failures about which bytes a claim meant: stale test servers,
patches against a moving page, files edited after their seal, K1 tokens committed blind. Authority was the weakest
layer: merges went ahead on chat authority, and the first preview merge reached main 20 minutes before the first
two-phone result. The harness stamped times without reading the clock (about a quarter to a third of self-written
stamps were later than the post; the worst +118 minutes) and corrected twelve comments and five log entries in place.
(SYNTHESIS.md; OVERNIGHT.md:47; OVERNIGHT.md:49)

Protocol v2 was proposed at 01:35 UTC and is NOT adopted: seals on every claim, one writer per path, a posting helper
and a commit gate that run K1 and refuse "@" bodies and placeholders, DECISION, RELAY and DELEGATION types with ACCEPT
naming its object, two identities with branch protection. PROTOCOL.md is unchanged. (PROTOCOL-v2-proposal.md:1;
#11/c6567020825)

Counts of the record: issue #10 holds 159 comments, #11 holds 9, #9 holds 10 (10:29 UTC). The ledger's last refresh
(03:25 UTC) counted 26 open asks between agents on the link, 17 in files, and 16 open owner asks. (LEDGER.md:7)

## 5. Agents used

By model and role, as named in the briefs and on the link. Fable: 10 Android auditors on NL-009 (FABLE-01 to -10, ten
FINDINGs on #9); 10 roadmap agents on NL-010 (five teams of two, FABLE-T1A to -T5B); 2 overnight watchers (Watcher A
release, Watcher B integration, the Fable controller stopped at 01:05 UTC on "Work with opus only agents"); 3
finalisers now (FABLE-FIN-1, -2, -3); and the harness session itself. Opus: 40 module agents in ten teams of four
(OPUS-1 to -10), raised to 50 with teams 11 to 13 (homepage card, See Through reader, served-domain check); 12 NL-011
link agents (six studies, six link runners); 4 admission controllers (OPUS-CONTROLLER 1 to 4, each a loop of about
three hours); 2 verify agents (Edition 5, Edition 6). On the link itself, 47 agent labels posted the 178 comments of
#9, #10 and #11: 21 Fable, 25 Opus and the harness; the harness alone wrote 24 of them. (BRIEF.md:5; OPUS-BRIEF.md:1;
OVERNIGHT.md:3; OVERNIGHT.md:41; OVERNIGHT.md:44; FIXES/NL-011/BRIEF.md; KUIPER-MAP.md section A)

## 6. Open owner decisions, each with a recommended answer

1. Adopt protocol v2 (#11/c6567020825 item 1). Recommended: adopt hunks 1 to 9 and 11 now (comments for events, the
   posting helper, the tightened envelope, seals, one writer per path, admissions and authority on the bus, K1 on
   comments); hunk 10 (two identities, branch protection on main) when you can set it up.
2. Purge the seven K1-flagged blobs from the history of branch edition/202611012135 (#11/c6567020825 item 2; the
   harness left them, #10/c6566977283). Recommended: purge, once the See Through module has landed, by rewriting that
   one branch (it never reached main); until then no agent merges the branch's history, only path checkouts.
3. Confirm or narrow the release delegation (#10/c6566796733; renewed and widened #10/c6567437030). Recommended:
   confirm it narrowed to: new dated kuiper-belt edition and See Through folders shipped only from a GREEN row naming
   a commit; the pointer moves; homepage changes limited to the Kuiper and See Through entries; expiry when the
   roadmap's module list is complete or at your word.
4. Q1, the elements repository's licence (ROADMAP.md:1011). The periodic-table layer stays REFUSED until answered.
   Recommended: Apache-2.0 for code and CC BY 4.0 for text, as every sibling repository; add the LICENSE file there.
5. Q5, the spider graph data's terms (ROADMAP.md:1023). Recommended: state the licence at the source (stars, testcode)
   the same way; until then the copied graphs stay marked DISCLOSED and are drawn, not relicensed.
6. Q7, the See Through slot on a phone (ROADMAP.md:1029; the breakpoint is now 434 px, so Pixel 7 at 412 px and
   Galaxy S24 at 360 px both show the bottom-left strip, #10/c6566607555). Recommended: keep the strip; it measured
   green on both phones in Editions 6 to 11, and a title at every width costs GridAtlas's face.
7. The page zoom lock: the viewport carries maximum-scale=1 and user-scalable=no in every shipped edition, which WCAG
   1.4.4 disallows (LEDGER.md row OW-zoom; kb@94aa593 editions/202611021017/index.html:5). Recommended: keep it until
   a candidate without it passes the pinch and spark-tap steps on both phones, then drop it in a new edition.
8. gridatlas PR #83 (the served check reports the Kuiper door, pointer and homepage row): open, cartridge-gate red on
   a lightning overlay test the PR does not touch (#10/c6567749539). Recommended: fix or re-run that test on main
   first, then merge #83; do not merge around a red gate.
9. The homepage entity whose text matches a K1 private digest (#10/c6567739175, served since restore point v136, not
   changed tonight). Recommended: decide whether that name is public; if not, change the homepage text and cut a new
   restore point; if it is, add its digest to the K1 allow-list so the check stops flagging it. The name is not
   written here.
10. Phase 2, the Kuiper paradigms, gated on your acceptance of steps 1 to 10 (ROADMAP.md:784). Recommended: accept
    Editions 5 to 11 as steps 1 to 4 and 6 to 8 delivered, with step 5's module and step 9's debts named as open,
    and start 8a with a per-app Kuiper of See Through.
11. Smaller: Q2 galaxies-wafers licence (Phase 2 only), Q3 a K5 line in ci_check or the separate edition_check (the
    separate tool exists), Q4 the denominators of the Kuiper that counts everything, Q6 who merges previews (moot
    under the delegation), Q8 the VENTUS mark wording in NOTICE.md (recommended: confirm as written), the lockup
    flanks above 700 px, and the 17 GPL and 48 unstated one-line quotations in elements.json as citations
    (recommended: confirm as citations). (ROADMAP.md:1015; LEDGER.md rows OW-lockup, OW-quotes)

## 7. Known debts

- edition_check on every Edition 6+ folder: E3 FAIL (edits under editions/202611012135/handoff after the cut, and
  the admitted files until the harness re-cuts the proof at ship), E6 FAIL (the loader reference copy still carries
  KY_EDITION 202611012135), E7 FAIL (prose instead of literals in the drift and three apps record entries); E9 is
  NOT EVALUATED where no clones sit under the snapshot root, and the recorded drift.json differs from one recomputed
  on another machine. (#10/c6572503742; #10/c6574630072; #10/c6570675769)
- The layers module's See Through stars row says "Edition 9 carries no data/see-through.json": the edition number is
  written into the module text; the next revision should read it from KY. (#10/c6572568222; #10/c6574744989)
- The File module's evidence is thinner than its first draft: seven shipped files measured live, but no key round-trip
  summary, no licence register and no journey record; NOTICE.md points to a LICENCES.md "when it lands".
  (#10/c6574630072)
- apps.json and elements.json carry edition 202611012135 in their own edition field, which apps.js does not read.
  (#10/c6570675769)
- The See Through module (star layer) is refused with no revision; the See Through page was not run on Galaxy S24;
  #repo lights amber not cyan; the line-of-code note clips at 404 px. (#10/c6567437030)
- The edition branch's own CI check is red since 03:20 UTC (law check, stray and pre-cut files). (run 41427484228)
- LAWS.md L11 (the card law) is still a patch in handoff/02-card, not applied on kuiper-belt main.
- Closed, for the record: the loader reference defect of the first preview (main e92ad5d carried rev 5 bytes
  d9272b82 against a manifest naming 25a16f1d) is gone; on main the reference file in Editions 5 and 11 hashes to
  25a16f1d, as the manifest says (measured 10:46 UTC). The E6 failure above is about the KY_EDITION stamp inside that
  reference copy, not its bytes. (OVERNIGHT.md:48; kb@94aa593)

## 8. What happens next

The See Through star-layer module needs a tester-passed revision; it would be Edition 12 by the same process. Teams 3
and 7 owe the E7 literals and the "Edition 9" text; team 4 owes a loader reference under a new stamp so E6 passes.
The owner's answers in section 6 unblock the periodic table (Q1), the spider terms (Q5), Phase 2 and protocol v2.
FABLE-FIN-1's FINDING and FABLE-FIN-2's REVIEW on #10 are folded into the final version of this report.

## 9. The Kuiper method applied to the link, and the Ventus grid engine for new links

Added at the owner's request this morning. FIXES/NL-011/KUIPER-MAP.md keys every rule, ruling, decision, handoff,
revision, review and finding of this repository and of issues #9, #10 and #11 the way the Kuiper keys lines: one row
per key, `nl@<commit> path:line` for a file line (the commit that wrote it, from git blame, the line re-read from that
commit) or `#<issue>/c<id>` for a comment, with who wrote it, when (UTC, GitHub's time for comments), its type and
what it superseded. Built by FIXES/NL-011/build_kuiper_map.py. The numbers in this report trace to those rows.

The map holds 271 file keys (all 271 re-read from their commits and equal to the working tree) and 178 comment keys
(#9 10, #10 159, #11 9), and 47 agent labels. (KUIPER-MAP.md:1)

The Ventus grid engine's graph format fits. Read at ventus-grid-engine@96a800eb01825748936b5a193ce396a960f9302f
(read only, nothing pushed): genome/build-graph.mjs writes genome/engine-graph.json as one object with schema, label,
generated_utc, note, focus_default, kind_labels, nodes, node_ids, edges and edge_kind_counts; a node is {label, type,
rag, reason, gh}; an edge is {from, to, type, evidence {file, lines, method}} with from and to as indices, written by
name and checked ("unknown edge.from" throws, build-graph.mjs:365), and evidence is mandatory (build-graph.mjs:201).
The spider receiver spider-sandbox.html reads any manifest graph through normaliseGenericGraph (spider-sandbox.html:238):
label, type, rag, reason, gh from each node, edges by index or id with any type string, so a graph of agents, issues,
rules and hand-offs joined by "replied to", "superseded" and "admitted" edges needs no change to the page or the
format. Two limits, both cosmetic and keyed: an edge type outside data, governance, archive, external, repo, workflow
is drawn in the default colour and labelled by its own name (spider-sandbox.html:176, :178), and a node type outside
the BADGE table shows the badge REPO (spider-sandbox.html:177), so an agent card reads REPO above its name; the rag
colours green, amber, red, grey, blue all work (spider-sandbox.html:175).

FIXES/NL-011/link-graph.json is written in exactly that shape by FIXES/NL-011/build_link_graph.py from the map: 499
nodes (3 issues, 47 agents, 178 comments, 271 file keys) and 677 edges (wrote 178, posted on 178, replied to 119,
superseded 47, admitted 11, refused 6, governs 138); its top-level keys, node keys and edge keys were compared to
engine-graph.json and are equal; every edge index is in range. rag: green in force, grey superseded, amber open or
asked of the owner, red refused. To draw it, the engine's spider/manifest.json needs one entry whose path is the raw
GitHub URL of link-graph.json (spider/README.md "How new graphs arrive"); that is a ventus-grid-engine commit and the
owner's call, so it was not made. Forming a new link from the graph then means picking an agent card and following
its "wrote" spokes to open hand-offs and the "replied to" spokes to who answered, which is what the next controller's
handover and the resume kit do by hand today.

---
_Generated by [Claude Code](https://claude.ai/code)_
