class Solution:

    def longestwithexact(self, nums, k):

        n = len(nums)
        curr_sum = 0
        longest = 0
        left = 0

        for right in range(n):

            curr_sum += nums[right]

            if curr_sum == k:
                longest = max(longest, right-left+1)

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

        return longest