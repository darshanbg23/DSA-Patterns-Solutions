class Solution:
    def maxCon1and0(self, nums):

        n = len(nums)

        longest = 0

        for i in range(n):

            zeros = 0

            for j in range(i,n):

                if nums[j] == 0:
                    zeros += 1

                if zeros > 1:
                    break

                longest = max(longest, (j-i)+1)

                
        return longest