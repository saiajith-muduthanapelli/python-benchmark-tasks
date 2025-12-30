from benchmarks.task_02_performance_comparison import buggy, fixed


def test_top_k_sum_matches_between_versions() -> None:
    values = [5, 1, 9, 3, 7]
    k = 3

    buggy_sum = buggy.compute_top_k_sum(values, k)
    fixed_sum = fixed.compute_top_k_sum(values, k)

    assert buggy_sum == fixed_sum == sum(sorted(values, reverse=True)[:k])
    assert values == [5, 1, 9, 3, 7]  # input not mutated


def test_handles_k_larger_than_input() -> None:
    values = [1, 2]
    assert buggy.compute_top_k_sum(values, 5) == fixed.compute_top_k_sum(values, 5) == 3
