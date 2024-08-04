def constructTree(pre, preLN, n):
    if n==1:
            node = Node(pre[0])
            return node
        
    q= []
        
    for i in range(n):
            node = Node(pre[i])
            if i == 0:
                root = node
            if len(q) > 0:
                last_node = q[-1]
                if last_node.left is None:
                    last_node.left = node
                elif last_node.right is None:
                    last_node.right = node
                    q.pop()
            if preLN[i] == 'N':
                q.append(node)
            
    return root