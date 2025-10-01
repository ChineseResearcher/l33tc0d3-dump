# linked list - medium
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            posSum = digit1 + digit2 + carry
            digit = posSum % 10
            carry = posSum // 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # We start off with a dummy head, so in the end we will ignore it
        return dummyHead.next