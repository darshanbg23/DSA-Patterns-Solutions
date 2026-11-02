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

| # | Problem | Solution |
|---|---|---|
| 1 | [Maximum Sum Subarray of Size K](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1) | [Solution](./1%20-%20Maximum%20Sum%20Subarray%20of%20Size%20K/) |
| 2 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Solution](./2%20-%20Maximum%20Average%20Subarray%20of%20Size%20K/) |
| 3 | Minimum Sum Subarray of Size K | [Solution](./3%20-%20Minimum%20Sum%20Subarray%20of%20Size%20K/) |
| 4 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | [Solution](./4%20-%20Maximum%20Number%20of%20Consecutive%201s/) |
| 5 | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) | [Solution](./5%20-%20Maximum%20Consecutive%201s%20With%20One%200%20Allowed/) |
| 6 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | [Solution](./6%20-%20Maximum%20Consecutive%201s%20with%20k%20zeros/) |
| 7 | Longest Subarray With Sum ≤ K | [Solution](./7%20-%20Longest%20Subarray%20With%20Sum%20%E2%89%A4%20K/) |
| 8 | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | [Solution](./8%20-%20Longest%20Subarray%20With%20Sum%20Exactly%20K/) |
| 9 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [Solution](./9%20-%20Minimum%20Size%20Subarray%20Sum/) |
| 10 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](./10%20-%20Longest%20Substring%20Without%20Repeating%20Characters/) |
| 11 | [Longest Substring With At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | [Solution](./11%20-%20Longest%20Substring%20With%20At%20Most%20K%20Distinct%20Characters/) |
| 12 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Solution](./12%20-%20Longest%20Repeating%20Character%20Replacement/) |
| 13 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | [Solution](./13%20-%20Subarray%20Product%20Less%20Than%20K/) |