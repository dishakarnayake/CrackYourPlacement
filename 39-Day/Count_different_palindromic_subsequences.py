class Solution(object):
    def countPalindromicSubsequences(self, s):
        n=len(s)
        mod=10**9+7
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
            if i+1<n:
                dp[i][i+1]=2
        for g in range(2,n):
            for i in range(n):
                j=i+g
                if j>=n:
                    break
                if s[i]!=s[j]:
                    dp[i][j]=dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                elif s[i:j+1].count(s[i])==2:
                    dp[i][j]=2*dp[i+1][j-1]+2
                elif s[i:j+1].count(s[i])==3:
                    dp[i][j]=2*dp[i+1][j-1]+1
                else:
                    s1=s[i+1:j]
                    x=i+s1.index(s[i])+2
                    y=j-s1[::-1].index(s[i])-2
                    dp[i][j]=2*dp[i+1][j-1]-dp[x][y]
                dp[i][j]%=mod
        return dp[0][n-1]