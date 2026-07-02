# dp - medium
from typing import List
from functools import cache
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) top-down DP with "src" as the starting point
        # 2) each subproblem is identified by (i, k), where k is the remaining
        # stops that we are allowed to have

        g = defaultdict(list)
        for u, v, c in flights:
            g[u].append((v,c))

        @cache
        def f(i:int, k:int) -> int:

            if i == dst: return 0

            res = float('inf')
            for j, c in g[i]:
                nk = k - 1 if j != dst else k
                if nk >= 0:
                    res = fmin(res, c + f(j, nk))

            return res

        res = f(src, k)
        return res if res < float('inf') else -1
    
n, flights, src, dst, k = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
n, flights, src, dst, k = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0
n, flights, src, dst, k = 4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1

Solution().findCheapestPrice(n, flights, src, dst, k)