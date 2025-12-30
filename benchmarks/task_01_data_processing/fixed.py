from __future__ import annotations

from typing import Dict, Iterable, List

Record = Dict[str, object]


def _safe_float(value: object) -> float | None:
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def aggregate_by_category(records: List[Record]) -> Dict[str, float]:
    """Compute average numeric value per category without mutating input."""
    valid_records = []
    for rec in records:
        numeric = _safe_float(rec.get("value"))
        if numeric is None:
            continue
        valid_records.append({"category": rec.get("category", "unknown"), "value": numeric})

    totals: Dict[str, float] = {}
    counts: Dict[str, int] = {}
    for rec in valid_records:
        cat = str(rec["category"])
        value = float(rec["value"])
        totals[cat] = totals.get(cat, 0.0) + value
        counts[cat] = counts.get(cat, 0) + 1

    return {cat: totals[cat] / counts[cat] for cat in totals}
