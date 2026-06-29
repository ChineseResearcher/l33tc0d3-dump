# sliding window - medium
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        n = len(customers)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) move a fixed-size sliding window with length "minutes"
        # since the secret technique has to be applied in consecutive blocks
        # 2) pre-compute prefix sums of satisfaction so as to make
        # satisfaction accounting more efficient when sliding window

        pf_sum = [0] * n
        if grumpy[0] == 0:
            pf_sum[0] = customers[0]

        for i in range(1, n):
            pf_sum[i] = pf_sum[i-1] + (customers[i] if grumpy[i] == 0 else 0)

        # slide window
        windowSum = 0
        for i in range(minutes):
            windowSum += customers[i]

        ans = pf_sum[-1] - pf_sum[minutes-1] + windowSum
        for r in range(minutes, n):
            windowSum += customers[r]
            windowSum -= customers[r-minutes]
            ans = fmax(ans, pf_sum[-1] - (pf_sum[r] - pf_sum[r-minutes]) + windowSum)

        return ans
    
customers, grumpy, minutes = [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3
customers, grumpy, minutes = [10,1,7], [0,0,0], 2
customers, grumpy, minutes = [4,10,10], [1,1,0], 2

Solution().maxSatisfied(customers, grumpy, minutes)