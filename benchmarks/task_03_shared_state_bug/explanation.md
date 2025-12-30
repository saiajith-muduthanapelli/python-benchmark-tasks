# Task 03: Shared State Bug

## What is the bug?
- The function uses a mutable list as a default argument, so every call shares the same buffer.
- Events from past invocations leak into later ones, corrupting expected output.

## Why does it happen?
- Default arguments are evaluated once at function definition time in Python.
- Without creating a new list per call, the buffer persists and keeps growing.

## What does the fix change?
- Switches the default to `None` and creates a fresh list when no buffer is provided.
- Calls that need to share state must pass an explicit buffer; otherwise, each call is isolated.

## What do the benchmarks prove?
- The buggy version shows ever-increasing buffer sizes across runs, while the fixed version always returns a buffer of the intended size.
- Timings remain similar, but the visible state difference highlights the correctness risk of shared defaults.
