from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Dict, Iterable, List


def generate_records(count: int, invalid_ratio: float = 0.05) -> List[Dict[str, object]]:
    """Create synthetic records with optional invalid values."""
    categories = ["alpha", "beta", "gamma", "delta"]
    records: List[Dict[str, object]] = []
    for idx in range(count):
        category = random.choice(categories)
        value: object
        if random.random() < invalid_ratio:
            value = None if random.random() < 0.5 else ""
        else:
            value = round(random.random() * 100, 3)
        records.append({"id": idx, "category": category, "value": value})
    return records


def generate_numbers(count: int) -> List[int]:
    """Generate a list of random integers for performance tests."""
    return [random.randint(0, 10_000) for _ in range(count)]


def write_csv(path: str | Path, records: Iterable[Dict[str, object]]) -> None:
    """Write records to CSV with a stable schema."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id", "category", "value"])
        writer.writeheader()
        for row in records:
            writer.writerow(row)
