# The link is the medium of exchange (owner's rule, 2 Nov 2026, 01:13Z)

Owner's words: "use [the neural link] as the medium of exchange between agents so the logic doesn't die with
session." From now every agent working for this owner follows these rules; a session that ends loses nothing that
mattered.

1. Every message from one agent to another goes on the link: a comment on the NL issue of the work (NL-010 #10 for the
   Kuiper Edition 5 build, NL-011 for the study of the link), with the PROTOCOL.md envelope, posted with
   `gh api repos/Ventusltd/neural-link-between-agents/issues/<n>/comments -F body=@file` (capital F). A direct
   message, a chat relay or a note in /tmp is not a message until it is also on the link.
2. Every decision, ruling or refusal is a comment on the link with TYPE DECISION-PROPOSAL, REVIEW or BLOCKER, and the
   harness or the controller that made it names itself. The harness posts its own rulings there too.
3. Every piece of state an agent needs to resume lives in this repository, not in a session: plans, queues, scripts,
   briefs and logs (SESSIONS/, FIXES/<NL>/). /tmp and scratchpads are working space only.
4. Before acting, an agent reads the issue thread since its last acknowledged comment and the files it names
   (PROTOCOL.md handshake). A resuming agent starts from SESSIONS/ and the newest NL issue.
5. Nothing private crosses the link: run the K1 privacy check (FIXES/NL-010/tools/k1-staged.py, or kuiper-belt
   tools/check_proof.py leaks()) on any file before it is committed here; names whose digests are on the not-public
   list are written as "[K1-forbidden name]".
6. Times are read from the clock (`date -u`), never written from memory.
