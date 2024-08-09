#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

import sys
# Function to find the level of a given node present in a binary tree
def isNodePresent(root, node):
 
    # base case
    if root is None:
        return False
 
    # if the node is found, return true
    if root.data==node:
        return True
 
    # return true if the node is found in the left or right subtree
    return isNodePresent(root.left, node) or isNodePresent(root.right, node)
    
def findLevel(root, node, level):
 
    # base case
    if root is None:
        return -sys.maxsize
 
    # return level if the node is found
    if root.data == node:
        return level
 
    # search node in the left subtree
    left = findLevel(root.left, node, level + 1)
 
    # if the node is found in the left subtree, return the left child
    if left != -sys.maxsize:
        return left
 
    # otherwise, continue the search in the right subtree
    return findLevel(root.right, node, level + 1)
 
 
# Function to find the lowest common ancestor of given nodes `x` and `y`,
# where both `x` and `y` are present in a binary tree.
def findLCA(root, x, y):
 
    # base case 1: if the tree is empty
    if root is None:
        return None
 
    # base case 2: if either `x` or `y` is found
    if root.data == x or root.data == y:
        return root
 
    # recursively check if `x` or `y` exists in the left subtree
    left = findLCA(root.left, x, y)
 
    # recursively check if `x` or `y` exists in the right subtree
    right = findLCA(root.right, x, y)
 
    # if `x` is found in one subtree and `y` is found in the other subtree,
    # update lca to the current node
    if left and right:
        return root
 
    return left if left else right
 
# Function to find the distance between node `x` and node `y` in a
# given binary tree rooted at `root` node
def findDistance(root, x, y):
 
    # `lca` stores the lowest common ancestor of `x` and `y`
    # lca = None
 
    # # call LCA procedure only if both `x` and `y` are present in the tree
    # if isNodePresent(root, y) and isNodePresent(root, x):
        
    # else:
       
 
    # return distance of `x` from lca + distance of `y` from lca
    lca = findLCA(root, x, y)
    if lca is not None:
        return findLevel(lca, x, 0) + findLevel(lca, y, 0)
    return -sys.maxsize
class Solution:
    def findDist(self,root,a,b):
        return findDistance(root, a,b)
    
        #return: minimum distance between a and b in a tree with given root
        #code here



