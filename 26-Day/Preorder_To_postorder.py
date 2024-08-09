#User function Template for python3
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    #code here
    stack = []
    root = Node(pre[0])
    stack.append(root)
    i = 1
    while i < size:
        minValue = None
        while (stack != [] and pre[i] > stack[-1].data):
            minValue = stack.pop()
        if minValue is None:
            temp = stack[-1]
            temp.left = Node(pre[i])
            stack.append(temp.left)
        else:
            minValue.right = Node(pre[i])
            stack.append(minValue.right)
        i = i + 1
    return root
            
        
            
        



