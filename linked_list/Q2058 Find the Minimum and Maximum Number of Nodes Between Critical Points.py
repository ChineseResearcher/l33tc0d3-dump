# linked list - medium
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) validate critical point by checking local min/max
        # 2) use another pointer to reference the prev. index of critical point

        curr, prev, i, j, j0 = head, None, 0, -1, -1

        ans = [float('inf'), float('-inf')]
        while True:
            
            v = curr.val
            if prev and curr.next:
                
                locMax = v > prev.val and v > curr.next.val 
                locMin = v < prev.val and v < curr.next.val
                if locMax or locMin:
                    if j != -1:
                        ans[0] = fmin(ans[0], i-j)
                        ans[1] = i-j0
                    else:
                        j0 = i
                    # update reference to prev. critical pt
                    j = i

            if not curr.next: break
            prev = curr
            curr = curr.next
            i += 1

        return ans if ans[0] < float('inf') else [-1, -1]

head = [3,1]
head = [5,3,1,2,5,1,2]
head = [1,3,2,2,3,2,2,2,7]