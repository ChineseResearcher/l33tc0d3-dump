# dp - medium
from typing import List
import heapq
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        n = len(prices)
        # core ideas:
        # 1) use dp[i] to represent the min. number of coins if we are
        # to acquire all fruits up to i-th fruit
        # 2) maintain a minheap to always obtain the best transition
        dp = [float('inf')] * n

        # first fruit have to be purchased
        dp[0] = prices[0]
        ans = dp[0]

        minheap = [[dp[0], 0]]
        for i in range(1, n):

            # lazy-delete predecessors who "free" range have expired
            while minheap and i > 2 * minheap[0][1] + 1:
                heapq.heappop(minheap)

            # op1: purchase this fruit
            op1 = dp[i-1] + prices[i]
            heapq.heappush(minheap, [op1, i])

            # op2: take it as a free fruit
            op2 = minheap[0][0]

            dp[i] = min(op1, op2)
            ans += dp[i]

        return dp[-1]
    
prices = [3,1,2]
prices = [1,10,1,1]
prices = [26,18,6,12,49,7,45,45]

Solution().minimumCoins(prices)