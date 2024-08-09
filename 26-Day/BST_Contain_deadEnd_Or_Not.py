class Solution:
    def isDeadEnd(self, root):
        # Code here
        def is_dead_end_util(node, min_val, max_val):
            if not node:
                return False
            
            # If current node is a dead end
            if min_val == max_val:
                return True
            
            # Recur for left and right subtrees with updated ranges
            left_dead_end = is_dead_end_util(node.left, min_val, node.data - 1)
            right_dead_end = is_dead_end_util(node.right, node.data + 1, max_val)
            
            return left_dead_end or right_dead_end
        
        # Initial call with full valid range
        return is_dead_end_util(root, 1, float('inf'))
        