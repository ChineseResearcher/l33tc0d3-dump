# linked list - medium
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional['ListNode']) -> Optional['ListNode']:

        # key ideas:
        # 1) use two pointers with one traversing at double the speed of the other
        # 2) if the faster pointer fails to jump to curr.next.next, we know that the
        # first pointer is right before the middle node

        # single node case: remove head
        if not head.next: return None

        n1, n2 = head, head.next
        while True:

            if not n2.next or not n2.next.next:
                n1.next = n1.next.next
                break
            # move ahead
            n1 = n1.next
            n2 = n2.next.next

        return head

head = [2,1]
head = [1,2,3,4]
head = [1,3,4,7,1,2,6]