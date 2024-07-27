# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return
        
        length = 0
        current = head
        newHead = None
        firstNodesList = [] # list to store the list of first nodes of k grouped nodes
        while current:
            length = length+1
            current = current.next
        
        numberOfNodesToBeReversed = length - (length % k)

        i = 0
        current = head
        prev = head

        while i < numberOfNodesToBeReversed:
            reverseOperationCount = 0
            prev = current
            current = current.next

            while reverseOperationCount < k-1:
                if reverseOperationCount == 0:
                    firstNodesList.append(prev)
                
                temp = current.next
                current.next = prev
                prev = current
                current = temp

                reverseOperationCount = reverseOperationCount+1

            
            if i == 0:
                head = prev
            elif len(firstNodesList) != 0:
                firstNodePrevGroup = firstNodesList.pop(0)
                firstNodePrevGroup.next = prev #link the first node of prev group to the last node of current group
            
            i = i+k
            
        if len(firstNodesList) != 0:
            firstNodePrevGroup = firstNodesList.pop(0)
            firstNodePrevGroup.next = current

        
        return head