class Solution(object):
    def findDuplicates(self, nums):
        ans =[]
        n=len(nums)
        for x in nums:
            x = abs(x)
            if nums[x-1]<0:
                ans.append(x)
            nums[x-1] *= -1
        return ans
        
obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))