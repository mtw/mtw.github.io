import csv
import math
from collections import defaultdict
from statistics import mean

groups = defaultdict(list)
sample_condition = {}
seen = set()
with open("measurements.csv", newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    expected = ["sample_id", "condition", "technical_repeat", "value"]
    if reader.fieldnames != expected:
        raise ValueError("Unexpected CSV columns")
    for line, row in enumerate(reader, start=2):
        if None in row or any(v is None or not v.strip() for v in row.values()):
            raise ValueError(f"Malformed or incomplete row at line {line}")
        sample = row["sample_id"].strip()
        condition = row["condition"].strip()
        repeat = row["technical_repeat"].strip()
        if condition not in {"control", "treatment"} or repeat not in {"1", "2"}:
            raise ValueError(f"Unexpected condition or repeat at line {line}")
        if sample in sample_condition and sample_condition[sample] != condition:
            raise ValueError(f"Conflicting conditions for {sample}")
        sample_condition[sample] = condition
        key = (sample, repeat)
        if key in seen:
            raise ValueError(f"Duplicate sample/repeat: {key}")
        seen.add(key)
        value = float(row["value"])
        if not math.isfinite(value):
            raise ValueError(f"Non-finite value at line {line}")
        groups[(condition, sample)].append(value)

if not groups or any(len(values) != 2 for values in groups.values()):
    raise ValueError("Expected two technical repeats per sample")
sample_rows = [(condition, sample, mean(values))
               for (condition, sample), values in sorted(groups.items())]
by_condition = defaultdict(list)
for condition, sample, value in sample_rows:
    by_condition[condition].append(value)
if set(by_condition) != {"control", "treatment"} or any(
    len(values) != 3 for values in by_condition.values()
):
    raise ValueError("Expected three independent samples per condition")
summary = [(condition, len(by_condition[condition]), mean(by_condition[condition]))
           for condition in ("control", "treatment")]
control, treatment = summary[0][2], summary[1][2]
if control == 0:
    raise ValueError("Percentage change is undefined for a zero control mean")

for filename, header, rows in (
    ("sample_means.csv", ["condition", "sample_id", "mean"], sample_rows),
    ("summary.csv", ["condition", "n_samples", "mean"], summary),
):
    with open(filename, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
print(f"Difference: {treatment - control:.2f}")
print(f"Change relative to control: {100 * (treatment - control) / control:.2f}%")
