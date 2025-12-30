# Python Benchmark Tasks

Compact, reviewer-friendly benchmarks that contrast flawed and fixed Python implementations. The scenarios mirror issues often surfaced in AI-assisted code reviews: hidden correctness bugs, inefficient algorithms under scale, and subtle shared-state leaks. This repository is a frozen reference for external reviewers and AI benchmarking—no active experiments, only deterministic scripts.

Each task provides:
- Buggy and fixed implementations with identical public APIs
- Deterministic micro-benchmarks with clear runtime and speedup reporting
- Focused explanations of the defect and the fix
- Pytest suites for correctness (no timing assertions)

## Tasks
- Task 01: Inefficient data aggregation (mutation + O(n²)-style removals vs single-pass filtering)
- Task 02: Top-k computation at scale (repeated sorts vs heap-based selection)
- Task 03: Shared mutable default state (leaking buffers vs isolated calls)

## Data
- A small sample dataset lives at `data/large_dataset.csv` and is used by Task 01 for a deterministic sanity check.
- Synthetic data generators in `utils/` create larger workloads reproducibly (seeded in benchmarks).

## Why this matters for AI benchmarking and code review
- The bugs are realistic and minimal, making them suitable for evaluating whether AI reviewers can detect correctness risks and performance regressions.
- Benchmarks are deterministic and runnable via `python -m ...`, ensuring reproducible measurements across environments.
- Tests emphasize behavioral guarantees, separating functional validation from performance measurement.

## Running benchmarks
From the repo root:
```bash
python -m benchmarks.task_01_data_processing.benchmark
python -m benchmarks.task_02_performance_comparison.benchmark
python -m benchmarks.task_03_shared_state_bug.benchmark
```

Benchmarks use in-repo packages only (no `sys.path` hacks) and seed randomness for repeatability.

## Running tests
```bash
pytest
```

## Expectations for reviewers and AI agents
- No `sys.path` hacks; imports resolve via packages from the repo root.
- Benchmarks are opt-in scripts and are not executed by pytest.
- Tests are fast, deterministic, and focus on correctness of the fixed implementations only (no timing assertions).
- The codebase is intentionally small and stable to highlight review quality, not feature velocity.
