## Merge Sorted Array ( [LeetCode - 88](https://leetcode.com/problems/merge-sorted-array/) )

### Problem

Given two sorted integer arrays, merge them into one sorted array in place, using the extra space at the end of the first array.

### Examples

- Example 1:

  - Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  - Output: [1,2,2,3,5,6]

- Example 2:

  - Input: nums1 = [1], m = 1, nums2 = [], n = 0
  - Output: [1]

- Example 3:

  - Input: nums1 = [0], m = 0, nums2 = [1], n = 1
  - Output: [1]

### Constraints

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- 10^9 <= nums1[i], nums2[j] <= 10^9
