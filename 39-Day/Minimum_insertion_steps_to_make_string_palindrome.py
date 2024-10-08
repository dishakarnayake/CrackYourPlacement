class Solution(object):
    def minInsertions(self, s):
        n=len(s)
        s2=s[-1::-1]
        dp=[[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]
    

        