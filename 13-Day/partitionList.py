# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x) :
        slist = ListNode(0)
        blist = ListNode(0)
        small = slist
        big = blist

        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        
        small.next = blist.next
        big.next = None

        return slist.next