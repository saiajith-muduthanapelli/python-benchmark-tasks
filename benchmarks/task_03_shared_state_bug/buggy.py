from __future__ import annotations

from typing import List


def append_event(event: object, buffer: List[object] = []) -> List[object]:
    """Append an event to a buffer and return it."""
    # BUG: default list is shared across calls, so events from previous calls leak into later runs.
    buffer.append(event)
    return buffer
