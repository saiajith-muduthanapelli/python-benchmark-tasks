from benchmarks.task_01_data_processing import buggy, fixed


def test_buggy_drops_zero_and_mutates_input() -> None:
    records = [
        {"category": "alpha", "value": 0.0},
        {"category": "beta", "value": 2.0},
    ]
    original_len = len(records)

    result = buggy.aggregate_by_category(records)

    assert "alpha" not in result  # zero was dropped incorrectly
    assert len(records) < original_len  # input list was mutated


def test_fixed_keeps_zero_and_ignores_non_numeric() -> None:
    records = [
        {"category": "alpha", "value": 0.0},
        {"category": "alpha", "value": ""},
        {"category": "alpha", "value": 10},
        {"category": "beta", "value": "oops"},
        {"category": "beta", "value": 5},
    ]

    result = fixed.aggregate_by_category(records)

    assert result["alpha"] == 5.0  # average of 0 and 10
    assert result["beta"] == 5.0
    assert len(records) == 5  # input unchanged
