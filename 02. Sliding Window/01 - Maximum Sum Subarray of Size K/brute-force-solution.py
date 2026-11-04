class Solution:
    def maxSubarraySum(self, arr, k):
        
        n = len(arr)
        
        max_sum = 0
        
        for i in range(n - k + 1):
            
            curr_sum = 0
            
            for j in range(i, i + k):
                
                curr_sum += arr[j]
                
            max_sum = max(max_sum, curr_sum)
            
        return max_sum