import os

LINE = "Never checked. I promised twice."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-88 chars,
# not only whitespace, a single line. Fail loudly instead of shipping
# an invalid entry.
if not 1 <= len(LINE) <= 88 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-88 char single-line gate")
if not 1 <= len(LINE.split()) <= 5:
    raise SystemExit("entry line violates the 1-5 word gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
