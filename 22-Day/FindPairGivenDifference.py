
from typing import List

class Solution:
    def findPair(self, n, x , arr ) :
        seen = set()
        for num in arr:
            if num - x in seen or num + x in seen:
                return 1
            seen.add(num)
        return -1
    
obj = Solution()
print(obj.findPair(5, 2, [1,2,3,4,5,6,7,8,9,10]))