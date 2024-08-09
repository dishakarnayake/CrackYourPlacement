'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here
        
        tmp = root 
        while root!=None:
            if root.key <= key:
                root = root.right 
            else:
                suc.key = root.key
                root = root.left 
        while tmp!=None:
            if tmp.key >= key:
                
                tmp = tmp.left
            else:
                pre.key = tmp.key
                tmp = tmp.right 
        
        
