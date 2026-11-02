# Binary Search On Answers

Binary Search on Answers is a pattern where we do not search for a specific value in a list. Instead, we search over a range of possible answers and test whether a candidate answer is feasible. For each midpoint, we check whether it satisfies the condition. If it is feasible, we keep the candidate and move the search toward a better answer; otherwise, we eliminate the corresponding half of the search space.

```python
def binary_search_on_answers(low, high):
    answer = -1

    while low <= high:
        mid = low + (high - low) // 2

        if is_feasible(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
```

## Problems

| # | Problem | Solution |
|---|---|---|
| 1 | [Find Square Root of a Number](https://leetcode.com/problems/sqrtx/) | [Solution](./1%20-%20Find%20Square%20Root%20of%20a%20Number/) |
| 2 | Find Nth Root of a Number | [Solution](./2%20-%20Find%20Nth%20Root%20of%20a%20Number/) |
| 3 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Solution](./3%20-%20Koko%20Eating%20Bananas/) |
| 4 | [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) | [Solution](./4%20-%20Find%20the%20Smallest%20Divisor%20Given%20a%20Threshold/) |
| 5 | Aggressive Cows | [Solution](./5%20-%20Aggressive%20Cows/) |
| 6 | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | [Solution](./6%20-%20Minimum%20Number%20of%20Days%20to%20Make%20m%20Bouquets/) |
| 7 | Allocate Minimum Number of Pages | [Solution](./7%20-%20Allocate%20Minimum%20Number%20of%20Pages/) |
| 8 | [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) | [Solution](./8%20-%20Minimum%20Speed%20to%20Arrive%20on%20Time/) |
| 9 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [Solution](./9%20-%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days/) |
| 10 | [Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) | [Solution](./10%20-%20Magnetic%20Force%20Between%20Two%20Balls/) |
