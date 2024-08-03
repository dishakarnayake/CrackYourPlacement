class Solution(object):
def connect(self, root):
    if root is None: return None
    dq, pre_level, pre_node = deque([(1, root)]), 0, None
    while dq:
        level, node = dq.popleft()
        if level == pre_level:  # current node is not the first node of level
            pre_node.next = node
            pre_node = node
        else:  # pre_level < level and node is the first node of level, then no need to update pre_node.next, 
            # leave it as None, update pre_node = node only.
            pre_level, pre_node = level, node
        if node.left:  # root is a perfect binary tree, once left exists, right must also exist
            dq.append((level + 1, node.left))
            dq.append((level + 1, node.right))
    return root