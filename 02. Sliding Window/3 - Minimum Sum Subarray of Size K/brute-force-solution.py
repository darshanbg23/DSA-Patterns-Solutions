class Solution:

    def minSumSubarr(self, nums, k):

        n = len(nums)
        
        mini_sum = float("inf")

        for i in range(n - k + 1):

            curr_sum = 0

            for j in range(i, i + k):
                curr_sum += nums[j]

            mini_sum = min(mini_sum, curr_sum)

        return mini_sum