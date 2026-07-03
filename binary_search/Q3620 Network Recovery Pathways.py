# binary search - hard
import heapq
from typing import List
from collections import defaultdict
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) binary search on the answer for maxi-min problem
        # 2) checker applies Djikstra's for shortest path

        g, maxEC = defaultdict(list), 0
        # build graph - exclude offline nodes
        for u, v, ec in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, ec))
            maxEC = fmax(maxEC, ec)

        def canReach(target:int) -> bool:
            # perform a constrained Djikstra's on the network of online nodes
            # with every edge traversed having weight >= target

            d = [float('inf')] * n
            d[0] = 0

            pq = [(0, 0)] # <node, cumuCost>
            while pq:

                i, c = heapq.heappop(pq)
                if c > d[i]:
                    continue

                if i == n-1: return c <= k

                for j, ec in g[i]:
                    # ensure min. edge weight >= target
                    if ec < target:
                        continue
                    nc = c + ec
                    if nc < d[j]:
                        d[j] = nc
                        heapq.heappush(pq, (j, nc))

        l, r, ans = 0, maxEC, -1
        while l <= r:
            mid = (l + r) >> 1
            if canReach(mid):
                ans = fmax(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans
    
edges, online, k = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], [True,True,True,True], 10
edges, online, k = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], [True,True,True,False,True], 12

Solution().findMaxPathScore(edges, online, k)