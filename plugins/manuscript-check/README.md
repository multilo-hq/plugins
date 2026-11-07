# manuscript-check

Check a manuscript before you submit it.

- `/manuscript-check:presubmit [journal or guidelines] [manuscript]` runs both checks below and gives one report.
- The `submission-checker` agent reads the journal's author guidelines and lists what breaks them: length, required sections and statements, title page, style, figures and tables. It only reads; it never edits.
- The `reference-consistency` skill checks that in-text citations, the reference list, figures, tables and other cross-references all match up.

## Install

In Multilo: Settings → Customize → Plugins → Discover, then **manuscript-check** → Install.
