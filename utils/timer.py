from __future__ import annotations

from contextlib import contextmanager
from time import perf_counter
from typing import Any, Callable, Generator, Iterable, Tuple


class Timer:
    """Context manager that measures elapsed wall time."""

    def __init__(self, label: str = "") -> None:
        self.label = label
        self.elapsed: float | None = None
        self._start: float | None = None

    def __enter__(self) -> "Timer":
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        if self._start is None:
            return
        self.elapsed = perf_counter() - self._start
        prefix = f"{self.label}: " if self.label else ""
        print(f"{prefix}{self.elapsed * 1000:.2f} ms")


def run_and_time(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Tuple[Any, float]:
    """Run `func` with timing, returning (result, elapsed_seconds)."""
    start = perf_counter()
    result = func(*args, **kwargs)
    elapsed = perf_counter() - start
    return result, elapsed


@contextmanager
def time_block(label: str = "") -> Generator[None, None, None]:
    """Convenient context manager for timing ad-hoc code blocks."""
    start = perf_counter()
    yield
    elapsed = perf_counter() - start
    prefix = f"{label}: " if label else ""
    print(f"{prefix}{elapsed * 1000:.2f} ms")
