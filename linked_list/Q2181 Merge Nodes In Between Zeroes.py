# linked list - medium
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # key ideas:
        # 1) use nodes with val = 0 as signposts to note end of summation
        # 2) use a pointer to reference the prev. node in the final modified LL

        # dummy head
        h = ListNode()

        prev, curr, intvlSum = h, head.next, 0
        while True:

            if not curr.val:
                prev.next = ListNode(val=intvlSum)
                intvlSum = 0 # reset
                prev = prev.next
            else:
                intvlSum += curr.val

            if not curr.next: break
            curr = curr.next

        return h.next  

head = [0,3,1,0,4,5,2,0] 
head = [0,1,0,3,0,2,2,0]