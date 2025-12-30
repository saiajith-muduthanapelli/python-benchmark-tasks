from __future__ import annotations

from typing import List, Optional


def append_event(event: object, buffer: Optional[List[object]] = None) -> List[object]:
    """Append an event to a fresh or provided buffer without sharing state."""
    if buffer is None:
        buffer = []
    buffer.append(event)
    return buffer
