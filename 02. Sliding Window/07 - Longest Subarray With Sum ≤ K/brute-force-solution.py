class Solution:

    def longsub(self, nums, k):

        n = len(nums)
        longest = 0

        for i in range(n):

            sums = 0

            for j in range(i,n):

                sums += nums[j]

                if sums > k:
                    break

                longest = max(longest, j-i+1)

        return longest