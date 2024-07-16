class Solution(object):
    def sortColors(self,nums):
        
        blue = white = red = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            elif i < red + white + blue:
                nums[i] = 2

        return nums

obj = Solution()
print(obj.sortColors([2,0,2,1,1,0]))