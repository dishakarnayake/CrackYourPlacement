
class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        # Initialize dp array with -1 (indicating no segments possible)
        dp = [-1] * (n + 1)
        
        # Base case: 0 segments can be made from a line of length 0
        dp[0] = 0
        
        # Fill the dp array
        for i in range(1, n + 1):
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        
        # If dp[n] is still -1, return 0, otherwise return dp[n]
        return max(dp[n], 0)