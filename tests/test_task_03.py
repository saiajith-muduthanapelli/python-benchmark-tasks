import importlib

from benchmarks.task_03_shared_state_bug import buggy, fixed


def test_buggy_leaks_between_calls() -> None:
    module = importlib.reload(buggy)
    first = module.append_event("a")
    first_len = len(first)
    second = module.append_event("b")
    assert first_len == 1
    assert len(second) == 2  # state carried over


def test_fixed_creates_fresh_buffer() -> None:
    importlib.reload(fixed)
    first = fixed.append_event("a")
    second = fixed.append_event("b")
    assert len(first) == 1
    assert len(second) == 1  # no leakage

    shared = []
    fixed.append_event("x", shared)
    fixed.append_event("y", shared)
    assert shared == ["x", "y"]  # explicit buffer still works
