class Solution:
    def minSubArrayLen(self, target, nums):
        
        n = len(nums)
        mini = float('inf')
        curr_sum = 0
        left = 0

        for right in range(n):
            
            curr_sum += nums[right]

            while curr_sum >= target:

                mini = min(mini, right-left+1)
                curr_sum -= nums[left]
                left += 1

        return mini if mini != float('inf') else 0