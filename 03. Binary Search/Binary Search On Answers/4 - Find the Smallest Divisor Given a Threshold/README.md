## Find the Smallest Divisor Given a Threshold ( [LeetCode - 1283](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) )

### Problem

Given an array of positive integers nums and a positive integer threshold, find the smallest divisor d such that dividing each element of nums by d and summing the ceil results is less than or equal to threshold.

### Examples

- Example 1:

  - Input: nums = [1,2,5,9], threshold = 6
  - Output: 5

- Example 2:

  - Input: nums = [2,3,5,7,11], threshold = 11
  - Output: 3

### Constraints

- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^6
- 1 <= threshold <= 10^6
