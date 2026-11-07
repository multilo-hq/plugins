---
name: reference-consistency
description: Use when checking that a manuscript's in-text citations, reference list, figures, tables and supplementary items all match up — before submission, after heavy editing, or when the user asks "are my references right?". Finds citations with no reference, references never cited, numbering out of order, and figures or tables cited but missing.
---
# Reference and cross-reference consistency

Check that everything the text points to exists, and that everything listed is pointed to. Report problems; do not fix them unless the user asks.

## 1. Find the citation style

Look at the first few citations:

- **Numbered** — `[1]`, `[1–3]`, `[2, 5]`, superscripts. Numbers must run in order of first citation (Vancouver and most medical journals), unless the reference list is alphabetical (some numbered styles are).
- **Author–year** — `(Smith, 2020)`, `Smith et al. (2020a)`. The reference list is alphabetical by first author.

If the manuscript mixes the two, report that first.

## 2. Citations against the reference list

Build two lists: every in-text citation, and every entry in the reference list.

- **Cited, not listed:** a citation with no matching reference. For author–year, match on first-author surname and year (and the `a`/`b` suffix).
- **Listed, not cited:** a reference never cited in the text, tables, figure legends or supplementary material.
- **Mismatch:** author–year citations whose spelling or year differs from the entry (`Smyth 2019` cited, `Smith 2019` listed); `et al.` used for a paper with two authors, or two names used for three or more, against the style's rule.
- **Numbered order:** the first citation of each number appears in increasing order; ranges (`[3–6]`) include every number in between; no number is skipped or used twice for different works.
- **Duplicates:** the same work listed twice (same DOI, or same title and year).

## 3. Figures, tables and supplementary items

- Every figure, table, box and supplementary item that exists is cited in the text, and the first citations come in order (Figure 1 before Figure 2).
- Every one cited exists, including panels (`Figure 2C` when Figure 2 has panels A–C).
- Supplementary items use one naming scheme (`Table S1` or `Supplementary Table 1`, not both).

## 4. Other cross-references

- Section references (`see Section 3.2`) point to a section that exists.
- Equation numbers cited exist.
- Abbreviations are defined at first use and then used consistently.

## Report

One line first: how many problems, or "No problems found".

Then group by type (citations, reference list, figures and tables, other). For each problem give the location (section and a short quote) and what is wrong. For numbered styles, give the expected number when it is out of order.

If the reference list is in a separate .bib or reference-manager file, say which file you read. If you could not read part of the manuscript (an image of a table, an embedded object), say so instead of guessing.
