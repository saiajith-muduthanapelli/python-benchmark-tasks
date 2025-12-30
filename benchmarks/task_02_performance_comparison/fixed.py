from __future__ import annotations

import heapq
from typing import Iterable


def compute_top_k_sum(values: Iterable[int], k: int) -> int:
    """Sum the top-k values efficiently using a heap."""
    top_k = heapq.nlargest(k, values)
    return sum(top_k)
