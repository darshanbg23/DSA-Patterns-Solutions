# Two Pointers

Two pointers is a pattern where we keep two indices moving through a collection to shrink the search space, compare values, or partition data without extra storage. It is commonly useful for sorted arrays, strings, and problems that need in-place updates or a linear scan with two moving fronts.

The basic intuition is to track two positions, usually left and right, and move them based on a comparison or a target condition until they meet or cross.

```python
def two_pointer_template(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1

    return None
```

## Problems

| # | Problem | Solution |
|---|---|---|
| 1 | [Reverse String](https://leetcode.com/problems/reverse-string/) | [Solution](./1%20-%20Reverse%20String/) |
| 2 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Solution](./2%20-%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted/) |