#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
       # Initialize an empty stack
        stack = []
        
        # Traverse the linked list
        current = head
        while current is not None:
            # While stack is not empty and the top element of stack is less than the current node's value
            while stack and stack[-1].data < current.data:
                stack.pop()
            # Push the current node onto the stack
            stack.append(current)
            # Move to the next node
            current = current.next
        
        # Reconstruct the linked list from the stack
        new_head = None
        if stack:
            new_head = stack[0]
            current = new_head
            for node in stack[1:]:
                current.next = node
                current = current.next
            current.next = None
        
        return new_head

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
