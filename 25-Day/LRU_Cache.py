class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key) :
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key, value) :
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict()
            
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _move_to_front(self, node) :
        # Remove node from current position
        node.prev.next = node.next
        node.next.prev = node.prev
        # Add node to front
        self._add_to_front(node)
    
    def _add_to_front(self, node) :
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def _evict(self):
        if len(self.cache) > 0:
            evict_node = self.tail.prev
            del self.cache[evict_node.key]
            evict_node.prev.next = self.tail
            self.tail.prev = evict_node.prev