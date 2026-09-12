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

