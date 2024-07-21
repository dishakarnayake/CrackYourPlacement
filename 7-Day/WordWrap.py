class Solution:
    	def solveWordWrap(self, nums, k):
            n = len(nums)
            dp = [float('inf')] * n
            
            for i in range(n):
                line_length = 0
                for j in range(i, n):
                    line_length += nums[j]
                    if line_length > k:
                        break
                    
                    if j == n - 1:
                        cost = 0
                    else:
                        spaces_left = k - line_length
                        cost = spaces_left * spaces_left
                    
                    if i == 0:
                        dp[j] = cost
                    else:
                        dp[j] = min(dp[j], dp[i-1] + cost)
                    
                    line_length += 1  # Add space between words
            
            return dp[n-1]
        
obj = Solution()
nums = [4, 2, 2, 5]
k = 6
print(obj.solveWordWrap(nums, k))