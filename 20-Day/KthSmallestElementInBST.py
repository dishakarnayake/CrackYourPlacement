class Solution:
    def kthSmallest(self, root, k) :
        stack = []
        current = root
        n = 0

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            n += 1
            if n == k:
                return current.val
            current = current.right
        
        return -1  # This return is just to satisfy the function signature, the function should always return within the loop if k is valid.