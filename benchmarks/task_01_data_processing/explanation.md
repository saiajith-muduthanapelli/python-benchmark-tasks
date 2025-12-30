# Task 01: Data Processing

## What is the bug?
- The buggy implementation removes items from the list while iterating, so some records are skipped.
- It treats any falsy value (including legitimate zeros) as invalid and drops them.
- Because it aliases the caller's list, the original data is mutated.

## Why does it happen?
- Using `if not rec.get("value")` conflates missing data with valid zero values.
- Removing items from the same list being iterated changes iteration order and hides some invalid entries.
- Assigning `cleaned = records` only copies the reference, so in-place removals affect the caller's list.

## What does the fix change?
- Validates values with a safe float conversion and filters without touching the input list.
- Keeps legitimate zeroes and only discards non-numeric entries.
- Processes a clean list in a single pass to build totals and counts.

## What do the benchmarks prove?
- The fixed version avoids quadratic-style removals and unnecessary list churn, so it runs faster on large inputs.
- Category averages from the fixed version include zero values and match expectations, while the buggy version can drop entire categories.
