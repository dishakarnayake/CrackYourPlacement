class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        maxSum = nums[0]
        curMin, curMax = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMin, curMax = curMax, curMin

            curMax = max(nums[i], curMax * nums[i])
            curMin = min(nums[i], curMin * nums[i])

            maxSum = max(maxSum, curMax)

        return maxSum
        