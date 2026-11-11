# results-table — publication-ready table template (run with `shell`).
#
# The agent edits the `# === EDIT ===` block and runs this. It prints a
# Markdown table (paste into the editor) or a LaTeX booktabs table (for
# submission). pandas is available in the Multilo's own Python.

import io
import pandas as pd

# ── === EDIT === ─────────────────────────────────────────────────────────────
DATA_CSV = """
group,score,latency_ms
A,0.812,124
A,0.799,131
B,0.741,158
B,0.755,149
"""

# Aggregate to mean ± SD per group? Set GROUP_BY + VALUE_COLS. Leave GROUP_BY
# empty ("") to format the raw rows instead.
GROUP_BY = "group"
VALUE_COLS = ["score", "latency_ms"]
SIG_FIGS = 3
OUTPUT = "markdown"      # "markdown" | "latex"
CAPTION = "Mean +/- SD by group."
# ── === END EDIT === ─────────────────────────────────────────────────────────

df = pd.read_csv(io.StringIO(DATA_CSV.strip()))


def fmt(x):
    try:
        return f"{float(x):.{SIG_FIGS}g}"
    except (TypeError, ValueError):
        return str(x)


if GROUP_BY:
    agg = df.groupby(GROUP_BY)[VALUE_COLS].agg(["mean", "std"])
    rows = []
    for grp, r in agg.iterrows():
        cells = [str(grp)]
        for col in VALUE_COLS:
            cells.append(f"{fmt(r[(col, 'mean')])} +/- {fmt(r[(col, 'std')])}")
        rows.append(cells)
    headers = [GROUP_BY] + VALUE_COLS
else:
    headers = list(df.columns)
    rows = [[fmt(v) for v in row] for row in df.itertuples(index=False)]

if OUTPUT == "markdown":
    print(f"<!-- Table. {CAPTION} -->")
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join("---" for _ in headers) + " |")
    for r in rows:
        print("| " + " | ".join(r) + " |")
elif OUTPUT == "latex":
    print("% " + CAPTION)
    print("\\begin{table}[t]\n  \\centering\n  \\caption{" + CAPTION + "}")
    print("  \\begin{tabular}{" + "l" * len(headers) + "}")
    print("    \\toprule")
    print("    " + " & ".join(headers) + " \\\\")
    print("    \\midrule")
    for r in rows:
        print("    " + " & ".join(r) + " \\\\")
    print("    \\bottomrule")
    print("  \\end{tabular}\n\\end{table}")
else:
    raise ValueError(f"Unknown OUTPUT: {OUTPUT}")
