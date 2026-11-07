---
description: Audit a manuscript against a journal's author guidelines before you submit it
argument-hint: "[journal name, guidelines URL or file] [manuscript file]"
---
Run a pre-submission check of my manuscript.

What I gave: $ARGUMENTS

1. Work out the manuscript file and the guidelines from what I gave. If I named a journal but no guidelines, find that journal's official "Instructions for authors" page. If anything is still unclear, ask me one short question before starting.
2. Hand the audit to the `manuscript-check:submission-checker` agent with the manuscript path and the guidelines (URL or file path).
3. Then use the `manuscript-check:reference-consistency` skill on the same manuscript.
4. Give me one combined report: the blocking problems first, then the rest. Keep the agent's table. Do not edit the manuscript unless I ask.
