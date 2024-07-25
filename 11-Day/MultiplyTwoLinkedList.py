# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

MOD = 10**9+7

class Solution:
    def list_to_number(self, head):
        num = 0
        # MOD = 10**9 + 7
        current = head
        while current:
            num = (num * 10 + current.data) % MOD
            current = current.next
        return num
    
    def multiply_two_lists(self, head1, head2):
        # MOD = 10**9 + 7
        num1 = self.list_to_number(head1)
        num2 = self.list_to_number(head2)
        return (num1 * num2) % MOD