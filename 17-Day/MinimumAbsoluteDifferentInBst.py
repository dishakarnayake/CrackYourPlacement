# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root) :
        self.prev = None
        self.ans = float('inf')
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev :
                self.ans = min(self.ans, root.val - self.prev.val)
            self.prev = root
            inorder(root.right)
            return
        
        inorder(root)
        return self.ans