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
| 3 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                   | [Solution](./3%20-%20Valid%20Palindrome/)                               |
