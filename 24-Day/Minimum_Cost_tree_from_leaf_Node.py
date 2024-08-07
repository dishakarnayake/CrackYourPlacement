class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
         # Initialize the result variable to hold the sum of non-leaf nodes' values
        res = 0
        # Use a stack to help with the construction of the tree
        stack = [float('inf')]

        # Iterate over each value in the array
        for num in arr:
            # While the current number is greater than the top of the stack,
            # it means we can form a non-leaf node with the smaller value on top of the stack
            while stack[-1] <= num:
                mid = stack.pop()
                res += mid * min(stack[-1], num)
            # Push the current number onto the stack
            stack.append(num)

        # After processing all numbers, there might be some values left in the stack
        # We need to process them as well to form the remaining non-leaf nodes
        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res