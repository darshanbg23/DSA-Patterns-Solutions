## Capacity To Ship Packages Within D Days ( [LeetCode - 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) )

### Problem

The package weights are given in an array weights, and the ship has a capacity limit. A ship can carry packages in consecutive segments, and each day you can ship at most one segment. Find the least capacity such that all packages can be shipped within D days.

### Examples

- Example 1:

  - Input: weights = [1,2,3,4,5,6,7,8,9], D = 5
  - Output: 15

- Example 2:

  - Input: weights = [3,6,7,11,12,14], D = 3
  - Output: 11

### Constraints

- 1 <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500
- 1 <= D <= weights.length
