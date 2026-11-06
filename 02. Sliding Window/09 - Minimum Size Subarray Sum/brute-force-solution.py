class Solution:
    def minSubArrayLen(self, target, nums):
        
        n = len(nums)
        mini = float('inf')

        for i in range(n):
            
            curr_sum = 0

            for j in range(i, n):

                curr_sum += nums[j]

                if curr_sum >= target:
                    mini = min(mini, j-i+1)
                    break

        return mini if mini != float('inf') else 0