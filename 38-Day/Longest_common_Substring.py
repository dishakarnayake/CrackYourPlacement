
class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        # Lengths of the two strings
        n = len(str1)
        m = len(str2)
        
        # Create a 2D array to store lengths of longest common suffixes
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Variable to store the maximum length of the common substring
        max_length = 0
        
        # Build the dp array from bottom up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Check if characters match
                if str1[i - 1] == str2[j - 1]:
                    # If they match, increase the length of the common substring
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    # If they don't match, reset the length
                    dp[i][j] = 0
        
        return max_length
