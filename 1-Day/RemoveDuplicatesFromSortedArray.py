class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
           print(0)

        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]

        return count + 1 
    

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,1,2,3,4,4]))