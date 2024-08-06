class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        node_map = {}
        current = head
        
        # First pass: Create a copy of each node and store it in the map
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        
        # Second pass: Connect the copied nodes' next and random pointers
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next
        
        return node_map[head]