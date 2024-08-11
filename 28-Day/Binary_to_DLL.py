#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        # Initialize previous node as None
        self.prev = None
    
    
    def bToDLL(self,root):
        if root is None:
            return root

        # Recursively convert left subtree
        head = self.bToDLL(root.left)

        # If the previous node is None, we're at the leftmost node
        if self.prev is None:
            # This node becomes the head of the DLL
            head = root
        else:
            # Modify the pointers to convert to DLL
            root.left = self.prev
            self.prev.right = root
        
        # Update the previous node
        self.prev = root

        # Recursively convert right subtree
        self.bToDLL(root.right)

        return head

# Helper function to print the DLL
def printDLL(head):
    while head:
        print(head.data, end=" ")
        head = head.right
