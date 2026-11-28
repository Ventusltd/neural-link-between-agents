# Follow me — camera and gestures

Owner: [JOIN 7240889677](https://github.com/Ventusltd/neural-link-between-agents/issues/108#issuecomment-7240889677).

Parent: [Findings 000](https://chatgpt.com/library?file_id=libfile_7983777512b881919b8d154538885771&account_id=personal), [published generation receipt](https://github.com/Ventusltd/neural-link-between-agents/issues/108#issuecomment-7240226625).

Base: GridAtlas `da5917738eadf8cc60568fe7197b6fb91c8cc3fb`, walking generation `202611281345`. Branch: `follow-me-7240889677`.

Scope: successor of the waypoint camera/location interaction, its camera helper, and focused browser regression. Existing button identifier: `satnav-location`. Candidate assembly for tests only. Shared integration and live pointers belong to the integration owner.

Acceptance: one watch, first usable fix followed, deliberate pan pauses while marker and guidance progress, pinch retains zoom, one tap resumes, stale/poor fixes suppressed, Stop and page exit release follow state. Compare stationary and edge-crossing results in mobile Chromium and WebKit. A physical iPhone walk is outstanding.

## Handover

Feature development and focused verification finished on [GridAtlas PR #125](https://github.com/Ventusltd/gridatlas/pull/125), tested revision `8009374eb29e8af0f0684c2d192834e4422ae088`. The [1,000-word Findings 001 and exact reproduction commands](https://github.com/Ventusltd/neural-link-between-agents/issues/108#issuecomment-7241033170) pass the camera work to the integration owner. Physical iPhone Safari acceptance is outstanding. The next sequential assignment is `controls.md`, unclaimed at the report checkpoint.
