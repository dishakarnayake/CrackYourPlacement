# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1,num2=0,0
        while l1!=None:
            num1=num1*10+l1.val
            l1=l1.next

        while l2!=None:
            num2=num2*10+l2.val
            l2=l2.next

        dummylist=dummy=ListNode(0)

        ans=str(num1+num2)
        for i in ans:
            dummy.next=ListNode(i)
            dummy=dummy.next

        return dummylist.next  