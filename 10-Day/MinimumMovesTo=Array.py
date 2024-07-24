class Solution:
    def minMoves2(self, nums):
        nums.sort()

        mid = nums[int(len(nums)/2)]
        count = 0
        for num in nums:
            count += abs(mid-num)
        
        return count
move = Solution()
print(move.minMoves2([1,2,3]))