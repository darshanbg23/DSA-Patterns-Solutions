## Koko Eating Bananas ( [LeetCode - 875](https://leetcode.com/problems/koko-eating-bananas/) )

### Problem

Koko loves to eat bananas. There are piles of bananas, and the i-th pile has piles[i] bananas. The guards have hired Koko to eat the bananas at a constant speed, and she can eat at most k bananas per hour. Each hour, Koko chooses a pile and eats k bananas from it (or the remaining bananas if the pile is smaller). Koko can only move to the next pile after finishing the current one. Find the minimum integer speed k such that Koko can finish all piles within h hours.

### Examples

- Example 1:

  - Input: piles = [3,6,7,11,12], h = 8
  - Output: 4

- Example 2:

  - Input: piles = [30,11,23,4,20], h = 5
  - Output: 30

### Constraints

- 1 <= piles.length <= 10^5
- 1 <= piles[i] <= 10^9
- 1 <= h <= 10^9
