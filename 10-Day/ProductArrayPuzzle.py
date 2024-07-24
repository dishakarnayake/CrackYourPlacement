#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        if n == 1:
            return [1]

        ans = [1] * n
        
        # left to right
        temp = 1
        for i in range(n):
            ans[i] *= temp
            temp *= nums[i]

        # reset temp to 1
        temp = 1

        # right to left
        for i in range(n - 1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans
obj = Solution()
print(obj.productExceptSelf([1,2,3,4],4))