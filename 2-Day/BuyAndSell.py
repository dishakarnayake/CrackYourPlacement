#using  Dynamic programming
class Solution(object):
   def maxProfit( self,prices):
 
        if not prices:
            return 0
        dp = [0] * len(prices)
        
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return dp[-1]
    
    
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))