from __future__ import annotations

from typing import Callable, List

from benchmarks.task_03_shared_state_bug import buggy, fixed
from utils.timer import run_and_time


def exercise(appender: Callable[[object], List[object]], iterations: int) -> int:
    last_size = 0
    for idx in range(iterations):
        buffer = appender({"id": idx})
        last_size = len(buffer)
    return last_size


def main() -> None:
    iterations = 20_000

    buggy_size, buggy_elapsed = run_and_time(exercise, buggy.append_event, iterations)
    fixed_size, fixed_elapsed = run_and_time(exercise, fixed.append_event, iterations)

    # Demonstrate leakage across separate calls.
    buggy_follow_up = buggy.append_event({"id": "extra"})
    fixed_follow_up = fixed.append_event({"id": "extra"})

    print(f"Buggy runtime: {buggy_elapsed * 1000:.2f} ms")
    print(f"Fixed runtime: {fixed_elapsed * 1000:.2f} ms")
    speedup = buggy_elapsed / fixed_elapsed if fixed_elapsed else float("inf")
    print(f"Speedup (buggy/fixed): {speedup:.2f}x")
    print(f"Buggy buffer size after first run: {buggy_size}")
    print(f"Fixed buffer size after first run: {fixed_size}")
    print(f"Buggy buffer size on follow-up call: {len(buggy_follow_up)}")
    print(f"Fixed buffer size on follow-up call: {len(fixed_follow_up)}")


if __name__ == "__main__":
    main()
