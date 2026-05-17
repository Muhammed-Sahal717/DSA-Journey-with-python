# Arrays — Structured Roadmap

A concise, practical roadmap for learning arrays and array-based problem patterns in Python.

## Overview

Arrays (lists in Python) are ordered collections of elements. They form the foundation for many algorithms and interview problems. This guide organizes topics from fundamentals to intermediate patterns with examples and practice problems.

## Phase 1 — Fundamentals

Core concepts to learn first:

- What is an array/list?
- Indexing (0-based)
- Traversal and iteration
- Insertion, deletion, updating values
- Length and slicing

Python quick examples:

```python
numbers = [10, 20, 30, 40]
print(numbers[0])        # access
numbers.append(50)       # insert at end
numbers.pop()            # remove last
for n in numbers:
    print(n)
```

## Phase 2 — Time Complexity

Understand the cost of common operations:

| Operation | Time Complexity |
|---|---:|
| Access by index | O(1) |
| Traversal (scan) | O(n) |
| Search (unsorted) | O(n) |
| Insert/Delete (end) | O(1) amortized |
| Insert/Delete (middle) | O(n) |
| Nested loops | O(n^2) |

Why it matters: picking the right pattern or auxiliary structure (hash, two pointers, etc.) often turns an O(n^2) approach into O(n) or O(n log n).

## Phase 3 — Important Array Patterns

These patterns appear repeatedly in interview problems. Learn the idea, implement, then practice several problems.

1. Linear Traversal

   - Use: find max/min, count occurrences, aggregate reductions.
   - Example tasks: Largest Element, Second Largest, Count Even Numbers.

2. Prefix Sum

   - Idea: precompute cumulative sums to answer range-sum queries quickly.
   - Example:

```python
arr = [1, 2, 3, 4]
prefix = [1, 3, 6, 10]
# range sum [i..j] = prefix[j] - prefix[i-1] (handle i=0)
```

   - Problems: Range Sum Query, Running Sum of 1D Array.

3. Two Pointers

   - Idea: use two indices moving toward each other (or in the same direction) on sorted arrays or when looking for pairs/subarrays.
   - Use for: sorted two-sum, move zeros, palindrome checks.
   - Example problem: Two Sum (sorted), Move Zeroes.

4. Sliding Window

   - Idea: maintain a window [i..j] and slide to find optimal subarray or substring (max, min, longest satisfying constraint).
   - Use for: max-sum subarray of fixed length, longest substring without repeating chars.

5. Hashing (Frequency / Lookup)

   - Idea: use dict/set to count or lookup in O(1). Great for frequency counts, complements, duplicates.
   - Problems: Two Sum, Contains Duplicate, Frequency Counter.

6. Sorting-Based Approaches

   - Idea: sometimes sorting simplifies the problem (pairs, intervals, grouping).
   - Problems: Merge Intervals, Sort Colors, k-th element variants.

## Phase 4 — Intermediate Topics

After mastering the above patterns, study:

- Kadane's algorithm (max subarray)
- Dutch National Flag / three-way partitioning
- Binary search on arrays (including rotated arrays)
- Monotonic stacks/queues
- Matrix (2D array) traversal patterns

## Best Learning Flow

For each topic:

1. Learn the concept and rationale.
2. Implement a brute-force solution.
3. Optimize to the best-known approach.
4. Solve 2–5 representative problems.
5. Write concise notes and code templates you can reuse.

## Practice Problems (starter list)

- Largest Element, Second Largest
- Two Sum (sorted and unsorted)
- Move Zeroes
- Running Sum / Prefix Sum queries
- Maximum Average Subarray
- Longest Substring Without Repeating Characters
- Merge Intervals
- Sort Colors

## Quick Reference: Useful Snippets

- Two pointers template (sorted two-sum):

```python
def two_sum_sorted(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return (i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    return None
```

- Sliding window template (variable size):

```python
def longest_unique_substring(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

## Notes

- Keep a small library of templates for each pattern.
- Practice under time constraints once comfortable with solutions.

---

Updated: cleaned structure, examples, and reference snippets.

If you want, I can add solution templates and example implementations for each practice problem. Which topic should I expand first?