
class Solution:
    def getCount(self,root,low,high):
# Base case: if root is None, return 0
        if root is None:
            return 0
        
        # Initialize the count
        count = 0

        # If the root's data lies within the range, count this node
        if low <= root.data <= high:
            count = 1
        
        # If root's data is greater than low, check the left subtree
        if root.data > low:
            count += self.getCount(root.left, low, high)
        
        # If root's data is less than high, check the right subtree
        if root.data < high:
            count += self.getCount(root.right, low, high)
        
        return count