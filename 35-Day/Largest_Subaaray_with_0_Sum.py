#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
         # Dictionary to store (cumulative sum: first occurrence index)
        cum_sum_map = {}
        max_len = 0
        cum_sum = 0
        
        for i in range(n):
            # Add current element to cumulative sum
            cum_sum += arr[i]
            
            if cum_sum == 0:
                # If cumulative sum is 0, we have a subarray from index 0 to i
                max_len = i + 1
            elif cum_sum in cum_sum_map:
                # If cumulative sum has been seen before, calculate the length
                max_len = max(max_len, i - cum_sum_map[cum_sum])
            else:
                # Store the cumulative sum with the current index
                cum_sum_map[cum_sum] = i
        
        return max_len
