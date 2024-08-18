#User function Template for python3

class Solution:
    def wordBreak(self, A, B):
        # Complete this function
        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and A[j:i] in B:
                    dp[i] = True
                    break
        
        return 1 if dp[n] else 0