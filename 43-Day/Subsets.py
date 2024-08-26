class Solution(object):
    def subsets(self, nums):
        if not nums:
            return []
        
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                curNum = res[i]
                res.append(curNum + [num])
                
        return res
        