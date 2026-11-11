---
name: results-table
description: 'Use when the user asks to make a results table, tabulate data, or compute group means/SDs from CSV/Excel. Markdown or LaTeX output.'
license: Apache-2.0
allowed-tools: Bash, Read, Write, Edit
metadata:
  file-types: data, markdown
  version: '1.1'
  icon: table
  keywords: table, results table, tabulate, summary statistics, mean, standard deviation, latex, markdown table, formatting
---

# Results table

Produce a clean, consistently-formatted results table (Markdown for the editor,
LaTeX `booktabs` for submission) from a data file.

## When to use
- "Make a results table from `data.csv`"
- "Tabulate the group means ± SD"
- "Format these numbers as a paper-ready table"

## Procedure
1. **Read the data** with `Read` (CSV/TSV and Excel). Decide what
   the rows and columns should be, and whether to aggregate (e.g. mean ± SD per
   group). Confirm with the user if the grouping is ambiguous — once.
2. **Adapt the template** [`./scripts/table.py`](./scripts/table.py): paste the
   data into `DATA_CSV`, set `GROUP_BY` / `VALUE_COLS` (or leave raw), choose
   `OUTPUT = "markdown" | "latex"`, and set significant figures.
3. **Run it with `Bash`** (`python table.py` — Multilo's own Python; pandas installs on demand). It prints the formatted table.
4. **Insert the Markdown table** into the document, or hand the LaTeX to the user
   for submission. Add a **numbered caption above the table** ("Table N. …").

## Formatting rules (consistency is everything)
- One decimal convention per column; align numbers on the decimal where possible.
- Report dispersion (± SD or 95% CI) next to every mean; state which in the caption.
- Mark significance with footnote symbols, not colour.
- Units in the column header, not in every cell.
- Use `booktabs` rules (top/mid/bottom) for LaTeX — never vertical lines.
