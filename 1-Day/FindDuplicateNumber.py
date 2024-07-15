class Solution(object):
    def findDuplicate(self, nums):
        
        a = set()

        for i in nums:
            if i in a:
                return i
            a.add(i)
        
obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))