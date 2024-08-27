class Solution:
    def findMaximumNum(self, s, k):
        # Convert string to a list of characters
        s = list(s)
        n = len(s)
        # Initialize the maximum number found as the current number
        max_num = [''.join(s)]
        
        def find_maximum_util(s, k):
            if k == 0:
                return
            
            for i in range(n):
                # Find the maximum digit in the remaining part of the string
                max_digit = max(s[i:])
                
                # If the current digit is not the maximum digit in the remaining part
                if s[i] != max_digit:
                    for j in range(i + 1, n):
                        # Swap with the rightmost maximum digit
                        if s[j] == max_digit:
                            # Swap characters at i and j
                            s[i], s[j] = s[j], s[i]
                            current_num = ''.join(s)
                            
                            # Update max_num if we found a larger number
                            if current_num > max_num[0]:
                                max_num[0] = current_num
                            
                            # Recurse with k-1 swaps
                            find_maximum_util(s, k - 1)
                            
                            # Backtrack to the original state
                            s[i], s[j] = s[j], s[i]
                    
                    # Since we only want to perform one successful swap per level
                    # if we found a better digit to swap, we break after one swap.
                    break
        
        find_maximum_util(s, k)
        return max_num[0]