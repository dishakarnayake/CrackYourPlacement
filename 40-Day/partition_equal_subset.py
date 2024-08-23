
class Solution:
    def equalPartition(self, N, arr):
        # code here
        total_sum = sum(arr)
        
        # If the total sum is odd, it's impossible to split the array into two equal sum parts
        if total_sum % 2 != 0:
            return 0
        
        # Target sum for one of the partitions
        target = total_sum // 2
        
        # Create a DP array to store if a sum can be formed or not
        dp = [False] * (target + 1)
        dp[0] = True  # We can always have a sum of 0
        
        # Process each element in the array
        for num in arr:
            # Traverse the dp array backward to ensure we do not reuse the same element
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # If dp[target] is True, a subset with the required sum exists
        return 1 if dp[target] else 0