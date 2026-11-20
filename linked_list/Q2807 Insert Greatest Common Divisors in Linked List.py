# linked list - medium
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def euc_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        curr, prev = head, None
        while curr is not None:
            if prev is not None:
                v = euc_gcd(prev.val, curr.val)
                nn = ListNode(val = v)
                prev.next = nn
                nn.next = curr
            prev = curr
            curr = curr.next

        return head

head = [7]
head = [18,6,10,3]