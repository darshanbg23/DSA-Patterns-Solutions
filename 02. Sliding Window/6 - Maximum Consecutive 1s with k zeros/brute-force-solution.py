class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        longest = 0

        for i in range(n):

            zeros = 0

            for j in range(i, n):

                if nums[j] == 0:
                    zeros += 1

                if zeros > k:
                    break

                longest = max(longest, j-i+1)

        return longest