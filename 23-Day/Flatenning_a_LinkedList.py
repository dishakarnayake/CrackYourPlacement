class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

class Solution:
    def mergeTwoLists(self, a, b):
        # If either list is empty, return the other list
        if a is None:
            return b
        if b is None:
            return a

        # Start with the linked list whose head data is the least
        if a.data < b.data:
            result = a
            result.bottom = self.mergeTwoLists(a.bottom, b)
        else:
            result = b
            result.bottom = self.mergeTwoLists(a, b.bottom)

        result.next = None  # We only use bottom pointers
        return result

    def flatten(self, root):
        # Base cases
        if root is None or root.next is None:
            return root

        # Recur for list on right
        root.next = self.flatten(root.next)

        # Merge this list with the list on right side
        root = self.mergeTwoLists(root, root.next)

        # Return the root
        return root

def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.bottom
    print("None")

# Driver code to test the above functions
if __name__ == "__main__":
    L = Node(5)
    L.bottom = Node(7)
    L.bottom.bottom = Node(8)
    L.bottom.bottom.bottom = Node(30)

    L.next = Node(10)
    L.next.bottom = Node(20)

    L.next.next = Node(19)
    L.next.next.bottom = Node(22)
    L.next.next.bottom.bottom = Node(50)

    L.next.next.next = Node(28)
    L.next.next.next.bottom = Node(35)
    L.next.next.next.bottom.bottom = Node(40)
    L.next.next.next.bottom.bottom.bottom = Node(45)

    sol = Solution()
    root = sol.flatten(L)
    printList(root)
