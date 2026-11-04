class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        max_count = 0
        
        for i in range(n):
            
            if nums[i] == 0:
                continue
            
            for j in range(i,n):
                
                if nums[j] == 0:
                    break
                
                max_count = max(max_count, j-i+1)
                
        return max_count