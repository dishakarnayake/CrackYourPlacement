# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        temp = head

        def findMiddle(temp):
            slow, fast = temp, temp
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        def reverseList(node):
            prev, curr = None, node
            while curr:
                nextTemp = curr.next
                curr.next = prev
                prev = curr
                curr = nextTemp
            return prev
        
        def mergeList(startP, midP):
            while midP:
                # store the next node
                startNext = startP.next
                midNext = midP.next

                # link node to second
                startP.next = midP

                # link mid to next node
                midP.next = startNext

                # mvoe pointer to the next one
                startP = startNext
                midP = midNext

        middle = findMiddle(temp)
        second_half = reverseList(middle.next)
        middle.next = None  # Split the list into two halves
        
        # Merge the two halves
        mergeList(head, second_half)       