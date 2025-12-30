from __future__ import annotations

from typing import Iterable, List


def compute_top_k_sum(values: Iterable[int], k: int) -> int:
    """Sum the top-k values using a slow repeated sort."""
    items: List[int] = list(values)
    total = 0
    for _ in range(min(k, len(items))):
        # BUG: sorts the entire list on every iteration and pops from the front, leading to O(n*k log n) time and extra allocations.
        items.sort(reverse=True)
        total += items.pop(0)
    return total
