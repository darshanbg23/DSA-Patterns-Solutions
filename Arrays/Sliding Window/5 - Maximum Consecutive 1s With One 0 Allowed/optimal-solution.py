class Solution:
    def maxCon1and0(self, nums):

        n = len(nums)
        longest = 0
        left = 0
        zeros = 0

        for right in range(n):

            if nums[right] == 0:
                zeros += 1

            while zeros > 1:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            longest = max(longest, (right-left)+1)
                
        return longest
