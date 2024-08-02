class Solution:
    def isValidBST(self, root) :
        def is_valid(node, min_val, max_val):
            if not node:
                return True
            
            if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False
            
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)
        
        return is_valid(root, float('-inf'), float('inf'))
obj = Solution()
print(obj.isValidBST([2,1,3]))