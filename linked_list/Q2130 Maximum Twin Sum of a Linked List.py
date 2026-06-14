# linked list - medium
from typing import Optional
class Solution:
    def pairSum(self, head: Optional['ListNode']) -> int:
        
        curr, values = head, []
        while True:
            
            values.append(curr.val)
            if curr.next:
                curr = curr.next
            else:
                break

        n, ans = len(values), 0
        for i in range(n // 2):
            ans = max(ans, values[i] + values[n-1-i])

        return ans
    
head = [1,100000]
head = [4,2,2,3]
head = [5,4,2,1]