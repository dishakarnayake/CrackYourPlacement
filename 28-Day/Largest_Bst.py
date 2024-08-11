class Solution:
    def largestBst(self, root):
        # Helper function to find largest BST
        def helper(node):
            if not node:
                return True, 0, float('inf'), float('-inf') # is_bst, size, min_value, max_value
            
            if not node.left and not node.right:
                return True, 1, node.data, node.data
            
            # Recursively traverse left and right subtrees
            left_is_bst, left_size, left_min, left_max = helper(node.left)
            right_is_bst, right_size, right_min, right_max = helper(node.right)
            
            # Check if the current subtree is a BST
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                # Current subtree is a BST
                size = left_size + right_size + 1
                return True, size, min(left_min, node.data), max(right_max, node.data)
            else:
                # Current subtree is not a BST, return the max size of the left or right subtree
                return False, max(left_size, right_size), 0, 0
        
        # Call the helper function on the root
        return helper(root)[1]