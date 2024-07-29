class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, start, end) :
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid - 1)
        root.right = self.helper(nums, mid + 1, end)
        
        return root