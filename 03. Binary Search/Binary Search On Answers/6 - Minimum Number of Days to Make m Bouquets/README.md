## Minimum Number of Days to Make m Bouquets ( [LeetCode - 1482](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) )

### Problem

You are given an integer array bloomDay, where bloomDay[i] is the day when the i-th flower blooms. You want to make m bouquets using the flowers, where each bouquet requires k adjacent flowers. Return the minimum number of days needed to make m bouquets, or -1 if it is impossible.

### Examples

- Example 1:

  - Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
  - Output: 3

- Example 2:

  - Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
  - Output: -1

### Constraints

- 1 <= bloomDay.length <= 10^5
- 1 <= bloomDay[i] <= 10^9
- 1 <= m <= 10^5
- 1 <= k <= bloomDay.length
