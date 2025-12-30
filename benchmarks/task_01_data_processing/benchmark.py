from __future__ import annotations

import random
from pathlib import Path

from benchmarks.task_01_data_processing import buggy, fixed
from utils.data_generator import generate_records
from utils.timer import run_and_time


def main() -> None:
    random.seed(0)
    dataset = generate_records(50_000, invalid_ratio=0.0)
    dataset.extend(
        [
            {"id": -1, "category": "alpha", "value": 0.0},
            {"id": -2, "category": "beta", "value": 0.0},
        ]
    )

    buggy_result, buggy_elapsed = run_and_time(buggy.aggregate_by_category, dataset.copy())
    fixed_result, fixed_elapsed = run_and_time(fixed.aggregate_by_category, dataset.copy())

    print(f"Buggy runtime: {buggy_elapsed * 1000:.2f} ms")
    print(f"Fixed runtime: {fixed_elapsed * 1000:.2f} ms")
    speedup = buggy_elapsed / fixed_elapsed if fixed_elapsed else float("inf")
    print(f"Speedup (buggy/fixed): {speedup:.2f}x")
    print(f"Buggy categories: {len(buggy_result)}")
    print(f"Fixed categories: {len(fixed_result)}")

    csv_path = Path("data/large_dataset.csv")
    if csv_path.exists():
        # Small deterministic run on the packaged sample file.
        import csv

        with csv_path.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        print("Sample CSV (buggy)", buggy.aggregate_by_category(rows))
        print("Sample CSV (fixed)", fixed.aggregate_by_category(rows))


if __name__ == "__main__":
    main()
