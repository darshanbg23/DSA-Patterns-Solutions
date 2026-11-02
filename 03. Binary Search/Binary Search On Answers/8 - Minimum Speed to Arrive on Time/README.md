## Minimum Speed to Arrive on Time ( [LeetCode - 1870](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) )

### Problem

You are given an integer array dist representing the distances along a route, and an integer hour. You must travel from the first train to the last one, where each train can move at some speed. Return the minimum integer speed such that you can reach the destination before or exactly at hour hours, where each distance can be traveled in time = distance / speed.

### Examples

- Example 1:

  - Input: dist = [1,3,2], hour = 6
  - Output: 1

- Example 2:

  - Input: dist = [1,3,2], hour = 2.7
  - Output: 3

### Constraints

- 1 <= dist.length <= 10^5
- 1 <= dist[i] <= 10^9
- 1 <= hour <= 10^9
