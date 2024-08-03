# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        internal_sum, external_sum = self.maxInternalAndExternalPathSums(root)
        return max(internal_sum, external_sum)
    
    def maxInternalAndExternalPathSums(self, node):
        
        # Case leaf
        # Internal path and extrnal path are the same
        if node.left == None and node.right == None:
            return node.val, node.val
        

        # Case not leaf
        left_internal = None
        left_external = None
        right_internal = None
        right_external = None
        if node.left != None:
            left_internal, left_external = self.maxInternalAndExternalPathSums(node.left)
        if node.right != None:
            right_internal, right_external = self.maxInternalAndExternalPathSums(node.right)

        # External sum
        external_sum = node.val
        if node.left != None:
            external_sum = max(external_sum, left_external + node.val)
        if node.right != None:
            external_sum = max(external_sum, right_external + node.val)
        
        # Internal sum
        internal_sum = external_sum # every external path can use as internal path
        if node.left != None and node.right != None:
            internal_sum = max(internal_sum, left_external + right_external + node.val)
        if node.left != None:
            internal_sum = max(internal_sum, left_internal, left_external)
        if node.right != None:
            internal_sum = max(internal_sum, right_internal, right_external)
        
        return internal_sum, external_sum