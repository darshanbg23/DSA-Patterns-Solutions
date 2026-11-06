# Sliding Window

The sliding window technique keeps track of a **contiguous part** of an array or string without repeatedly processing the same elements.

---

## Types of Sliding Window

### 1. Fixed Window

The window size stays constant and is usually given by `k`.

**Example:** Find the maximum sum of a subarray of size `k`.

```python
window_sum = 0

for i in range(k):
    window_sum += nums[i]

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - k]
```

---

### 2. Variable Window

The window size changes based on a condition. The window expands and shrinks as needed.

**Example:** Find the longest subarray whose sum is less than or equal to `limit`.

```python
left = 0
window_sum = 0

for right in range(len(nums)):

    window_sum += nums[right]

    while window_sum > limit:
        window_sum -= nums[left]
        left += 1
```

---

## Problems

### 1. Fixed Window

| # | Problem | Solution |
|---|---|---|
| 1 | [Maximum Sum Subarray of Size K](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1) | [Solution](./01%20-%20Maximum%20Sum%20Subarray%20of%20Size%20K/) |
| 2 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Solution](./02%20-%20Maximum%20Average%20Subarray%20of%20Size%20K/) |
| 3 | Minimum Sum Subarray of Size K | [Solution](./03%20-%20Minimum%20Sum%20Subarray%20of%20Size%20K/) |

### 2. Variable Window

| # | Problem | Solution |
|---|---|---|
| 1 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | [Solution](./04%20-%20Maximum%20Number%20of%20Consecutive%201s/) |
| 2 | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) | [Solution](./05%20-%20Maximum%20Consecutive%201s%20With%20One%200%20Allowed/) |
| 3 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | [Solution](./06%20-%20Maximum%20Consecutive%201s%20with%20k%20zeros/) |
| 4 | Longest Subarray With Sum ≤ K | [Solution](./07%20-%20Longest%20Subarray%20With%20Sum%20%E2%89%A4%20K/) |
| 5 | Longest Subarray With Sum Exactly K (Non-negative) | [Solution](./08%20-%20Longest%20Subarray%20With%20Sum%20Exactly%20K/) |
| 6 | [Minimum Size Subarray Sum (LeetCode 209)](https://leetcode.com/problems/minimum-size-subarray-sum/) | [Solution](./09%20-%20Minimum%20Size%20Subarray%20Sum/) |