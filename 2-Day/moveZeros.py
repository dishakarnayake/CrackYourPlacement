class Solution(object):
    def moveZeroes(self, nums):

        non_zero = 0 # index of first non-zero element
        for i in range(len(nums)): # loop through array
            if nums[i] != 0: # if element is not zero
                nums[i], nums[non_zero] = nums[non_zero], nums[i] # swap elements
                non_zero += 1
        return nums

obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))
        