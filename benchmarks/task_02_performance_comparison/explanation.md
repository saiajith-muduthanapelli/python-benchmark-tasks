# Task 02: Performance Comparison

## What is the bug?
- The buggy function repeatedly sorts the entire list and pops from the front, which costs O(n*k log n) and churns memory.
- Performance collapses as `k` or input size grows even though the desired result is simple.

## Why does it happen?
- Sorting inside the loop rebuilds order for every element of the top-k instead of selecting once.
- Popping from index 0 triggers list shifting, adding more overhead.

## What does the fix change?
- Uses `heapq.nlargest`, which is O(n log k) and allocates only what is needed for the top-k items.
- Single pass over the input and one summation.

## What do the benchmarks prove?
- On large inputs (hundreds of thousands of ints), the heap-based approach is significantly faster while returning the same sum.
