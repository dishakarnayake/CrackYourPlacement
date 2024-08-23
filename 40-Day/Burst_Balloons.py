class Solution:
    def maxCoins(self, nums) :
        if len(nums) == 1: return nums[0]
        nums = [1] + nums + [1]
        leng = len(nums)
        dp = [[0] * leng for _ in range(leng)]
        for i in range(leng-2,-1,-1):
            for j in range(i, leng):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k])
        return dp[0][leng-1]
        