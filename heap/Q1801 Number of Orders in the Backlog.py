# heap - medium
from typing import List
import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        # core ideas:
        # 1) use a minheap for sell orders
        # 2) use a maxheap for buy orders

        minheap, maxheap = [], []
        for op, q, ot in orders:

            # buy-order
            if ot == 0:

                if not minheap or minheap[0][0] > op:
                    heapq.heappush(maxheap, [-op, q])
                    continue

                # consume backlogged sell orders while tracking buy quantity
                while q > 0 and minheap and op >= minheap[0][0]:
                    sp, sq = heapq.heappop(minheap)
                    if q < sq:
                        heapq.heappush(minheap, [sp, sq-q])
                    q -= min(q, sq)

                if q > 0:
                    heapq.heappush(maxheap, [-op, q])

            # sell-order
            else:

                if not maxheap or abs(maxheap[0][0]) < op:
                    heapq.heappush(minheap, [op, q])
                    continue

                # consume backlogged buy orders while tracking sell quantity
                while q > 0 and maxheap and op <= abs(maxheap[0][0]):
                    bp, bq = heapq.heappop(maxheap)
                    if q < bq:
                        heapq.heappush(maxheap, [bp, bq-q])
                    q -= min(q, bq)

                if q > 0:
                    heapq.heappush(minheap, [op, q])

        ans, MOD = 0, int(1e9 + 7)
        # collect answer as the remaining order quantity
        for _, q in minheap:
            ans += q
            ans %= MOD

        for _, q in maxheap:
            ans += q
            ans %= MOD

        return ans
    
orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
orders = [[19,28,0],[9,4,1],[25,15,1]]

Solution().getNumberOfBacklogOrders(orders)