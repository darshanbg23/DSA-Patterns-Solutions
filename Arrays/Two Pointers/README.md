# Two Pointers

Two Pointers is a problem-solving pattern where two indices are used to traverse a collection while reducing the search space or processing elements efficiently. The pointers can move from opposite ends toward each other or move in the same direction, depending on the problem.

The movement of each pointer is controlled by the current condition of the problem. Instead of checking every possible pair or combination, the pointers are moved intelligently so that unnecessary comparisons are skipped.

This pattern is commonly useful for sorted arrays, strings, palindrome problems, in-place modifications, partitioning, and problems that require comparing elements from different positions.

A common approach is to maintain two pointers, `left` and `right`, and move one or both pointers based on the required condition.

```python
def two_pointers(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        # Process elements at left and right

        if condition_to_move_left:
            left += 1

        if condition_to_move_right:
            right -= 1

    return result
```

The exact pointer movement depends on the problem. The important idea is to determine **when and why each pointer should move** rather than blindly moving them.


## Problems

| # | Problem | Solution |
|---|---|---|
| 1 | [Reverse String](https://leetcode.com/problems/reverse-string/) | [Solution](./1%20-%20Reverse%20String/) |
| 2 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](./2%20-%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/) |
| 3 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Solution](./3%20-%20Valid%20Palindrome/) |
| 4 | [Remove Element](https://leetcode.com/problems/remove-element/) | [Solution](./4%20-%20Remove%20Element/) |
| 5 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Solution](./5%20-%20Remove%20Duplicates%20from%20Sorted%20Array/) |
| 6 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Solution](./6%20-%20Move%20Zeroes/) |
| 7 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [Solution](./7%20-%20Merge%20Sorted%20Array/) |
| 8 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | [Solution](./8%20-%20Squares%20of%20a%20Sorted%20Array/) |
| 9 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Solution](./9%20-%20Container%20With%20Most%20Water/) |
| 10 | [3Sum](https://leetcode.com/problems/3sum/) | [Solution](./10%20-%203Sum/) |
| 11 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Solution](./11%20-%203Sum%20Closest/) |
| 12 | [4Sum](https://leetcode.com/problems/4sum/) | [Solution](./12%20-%204Sum/) |
| 13 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Solution](./13%20-%20Trapping%20Rain%20Water/) |
