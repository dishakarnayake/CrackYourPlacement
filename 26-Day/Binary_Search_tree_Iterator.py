class BSTIterator:
    
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) :
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val
    
    def hasNext(self) :
        return len(self.stack) > 0