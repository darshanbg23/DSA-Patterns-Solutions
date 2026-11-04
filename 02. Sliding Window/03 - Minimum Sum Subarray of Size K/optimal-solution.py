class Solution:

    def minSumSubarr(self, nums, k):

        n = len(nums)

        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        mini_sum = curr_sum

        for i in range(k, n):

            curr_sum -= nums[i - k]
            curr_sum += nums[i]

            mini_sum = min(mini_sum, curr_sum)

        return mini_sum