class Solution:

    def longsub(self, nums, k):

        n = len(nums)
        longest = 0
        curr_sum = 0
        left = 0

        for right in range(n):

            curr_sum += nums[right]

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            longest = max(longest, right-left+1) 

        return longest