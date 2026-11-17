# dp - hard
from functools import cache
class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        
        INF = float('inf')
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) top-down dp w/ states (i, j, c):
        # - i: i-th house
        # - j: j-th neighbourhood
        # - c: colour of previous house (painted or original)
        # 2) for each unpainted house, try out colour in [1, n], and compute the
        # minimum of these options

        @cache
        def f(i: int, j: int, c: int) -> int:

            if j > target:
                return INF
            
            if i == m:
                return 0 if j == target else INF

            # already painted
            if houses[i] != 0:
                nj = j + 1 if houses[i] != c and c != -1 else j
                return f(i + 1, nj, houses[i])

            res = INF
            # try all colours
            for nc in range(n):
                nj = j + 1 if (nc + 1) != c and c != -1 else j
                res = fmin(res, cost[i][nc] + f(i + 1, nj, nc + 1))

            return res

        res = f(0, 1, -1)
        return res if res < INF else -1

houses, cost, m, n, target = [3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3
houses, cost, m, n, target = [0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3
houses, cost, m, n, target = [0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3

Solution().minCost(houses, cost, m, n, target)