# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        return slow
obj = Solution()
print(obj.middleNode([1,2,3,4,5]))
        