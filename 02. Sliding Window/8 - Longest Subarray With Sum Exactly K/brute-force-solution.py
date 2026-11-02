class Solution:

    def longestwithexact(self, nums, k):

        n = len(nums)
        longest = 0

        for i in range(n):

            sums = 0

            for j in range(i,n):

                sums += nums[j]

                if sums == k:
                    longest = max(longest, j-i+1)

                if sums > k:
                    break

        return longest

sol = Solution()
nums = [1, 2, 1, 1, 1, 3]
k = 4
print(sol.longestwithexact(nums, k))