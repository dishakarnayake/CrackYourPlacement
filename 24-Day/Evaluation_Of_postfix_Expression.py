class Solution:
    # Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        # Create an empty stack
        stack = []

        # Iterate over each character in the postfix expression
        for char in S:
            if char.isdigit():
                # If the character is a digit, push it onto the stack
                stack.append(int(char))
            else:
                # If the character is an operator, pop two elements from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Perform the operation and push the result back onto the stack
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(int(operand1 / operand2))  # Ensure integer division

        # The final result will be the only element left in the stack
        return stack.pop()

# Example usage:
solution = Solution()
postfix_expression = "231*+9-"
result = solution.evaluatePostfix(postfix_expression)
print(result)  # Output: -4
