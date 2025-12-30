from __future__ import annotations

import random

from benchmarks.task_02_performance_comparison import buggy, fixed
from utils.data_generator import generate_numbers
from utils.timer import run_and_time


def main() -> None:
    random.seed(0)
    values = generate_numbers(500_000)
    k = 50

    buggy_sum, buggy_elapsed = run_and_time(buggy.compute_top_k_sum, values, k)
    fixed_sum, fixed_elapsed = run_and_time(fixed.compute_top_k_sum, values, k)

    print(f"Buggy runtime: {buggy_elapsed * 1000:.2f} ms")
    print(f"Fixed runtime: {fixed_elapsed * 1000:.2f} ms")
    speedup = buggy_elapsed / fixed_elapsed if fixed_elapsed else float("inf")
    print(f"Speedup (buggy/fixed): {speedup:.2f}x")
    print(f"Buggy sum: {buggy_sum}")
    print(f"Fixed sum: {fixed_sum}")


if __name__ == "__main__":
    main()
