## Longest Subarray With Sum Exactly K

### Problem

Given an array `nums` containing non-negative integers and an integer `k`, find the length of the longest contiguous subarray whose sum is exactly equal to `k`.

### Examples

**Example 1:**
- Input: `nums = [1, 2, 3, 1, 1, 1, 1], k = 3`
- Output: `3`
- Explanation: The subarray `[1, 2]` has sum 3 and length 2, while `[3]` has length 1. The longest valid subarray is `[1, 1, 1]`, with length 3.

**Example 2:**
- Input: `nums = [1, 1, 1, 1, 1], k = 3`
- Output: `3`
- Explanation: The subarray `[1, 1, 1]` has sum 3 and length 3.

### Constraints

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9