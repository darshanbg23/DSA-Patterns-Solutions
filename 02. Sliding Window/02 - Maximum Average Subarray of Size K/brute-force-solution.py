class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        n = len(nums)
        
        max_avg = float('-inf')

        for i in range(n - k + 1):

            curr_sum = 0

            for j in range(i, i + k):

                curr_sum += nums[j]

            max_avg = max(max_avg, (curr_sum / k))

        return max_avg