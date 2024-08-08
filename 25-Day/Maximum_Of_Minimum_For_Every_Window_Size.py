#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        # Arrays to store previous and next smaller elements
        left = [-1] * n
        right = [n] * n
        
        # Create an empty stack
        stack = []
        
        # Fill elements of left[] using a stack
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        # Empty the stack
        stack = []
        
        # Fill elements of right[] using a stack
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        # Initialize the result array with 0
        result = [0] * n
        
        # Fill the result array
        for i in range(n):
            length = right[i] - left[i] - 1
            result[length-1] = max(result[length-1], arr[i])
        
        # Some entries in result[] may not be filled yet. Fill them by taking values from right side of result[]
        for i in range(n-2, -1, -1):
            result[i] = max(result[i], result[i+1])
        
        return result