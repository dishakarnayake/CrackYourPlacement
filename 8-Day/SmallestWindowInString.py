from collections import defaultdict

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return -1
        
        p_count = defaultdict(int)
        for char in p:
            p_count[char] += 1
        
        required_chars = len(p_count)
        formed_chars = 0
        
        window_counts = defaultdict(int)
        min_window = float('inf'), None, None
        
        left = 0
        for right in range(len(s)):
            character = s[right]
            window_counts[character] += 1
            
            if character in p_count and window_counts[character] == p_count[character]:
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                character = s[left]
                
                if right - left + 1 < min_window[0]:
                    min_window = (right - left + 1, left, right)
                
                window_counts[character] -= 1
                if character in p_count and window_counts[character] < p_count[character]:
                    formed_chars -= 1
                
                left += 1
        
        return -1 if min_window[0] == float('inf') else s[min_window[1] : min_window[2] + 1]