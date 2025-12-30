from __future__ import annotations

from typing import Dict, List

Record = Dict[str, object]


def aggregate_by_category(records: List[Record]) -> Dict[str, float]:
    """Compute average numeric value per category."""
    cleaned = records  # alias; mutates caller
    for rec in cleaned:
        # BUG: drops falsy values (removes legitimate zeros) while mutating during iteration, so some records are skipped and the caller's list is altered.
        if not rec.get("value"):
            cleaned.remove(rec)
    totals: Dict[str, float] = {}
    counts: Dict[str, int] = {}
    for rec in cleaned:
        value = float(rec["value"])
        cat = str(rec["category"])
        totals[cat] = totals.get(cat, 0.0) + value
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: totals[cat] / counts[cat] for cat in totals}
