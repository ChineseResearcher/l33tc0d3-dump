# greedy - hard
import math
from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
        # key ideas:
        # 1) propagate bound restrictions using a difference of 1 in both directions
        # 2) as n can be large (n <= 1e9), process the restrictions only
        # 3) the local "peaks" can be determined using intersection geometry
        # of the slopes involving two restricted heights next to each other

        r = [[1,0]] + restrictions
        r.sort()
        m = len(r)

        # assign the upper bounds at those restricted indices
        ub = [float('inf')] * m
        ub[0] = 0

        # track the curr. applicable bound
        curr = -1
        # right pass
        for i in range(1, m):

            curr = ub[i-1] + (r[i][0] - r[i-1][0])
            if r[i][1] < curr: curr = r[i][1]
            ub[i] = min(ub[i], curr)

        curr = -1
        # left pass
        for i in range(m-2, -1, -1):

            curr = ub[i+1] + (r[i+1][0] - r[i][0])
            if r[i][1] < curr: curr = r[i][1]
            ub[i] = min(ub[i], curr)

        def solve(x0:int, y0:int, x1:int, y1:int) -> int:
            # we are solving for the y-intersection of the two lines:
            # 1) y = x - x0 + y0
            # 2) y = -x + x1 + y1
            X = (x1 + y1 + x0 - y0) / 2
            # out of [x0, x1] range
            if X < x0: return -x0 + x1 + y1
            if X > x1: return x1 - x0 + y0
            # valid intersection 
            return math.floor(X - x0 + y0)

        ans = max(ub)
        # improve our answer with slope intersection heights
        # of an ordered pair of upper bounds
        for i in range(1, m):
            x0, y0 = r[i-1][0], ub[i-1]
            x1, y1 = r[i][0], ub[i]

            localMax = solve(x0, y0, x1, y1)
            ans = max(ans, localMax)

        # take care of last intersection (with imaginary x=n)
        ans = max(ans, n-r[-1][0]+ub[-1])

        return ans

n, restrictions = 6, []
n, restrictions = 5, [[2,1],[4,1]]
n, restrictions = 10, [[5,3],[2,5],[7,4],[10,3]]
n, restrictions = 10, [[8,5],[9,0],[6,2],[4,0],[3,2],[10,0],[5,3],[7,3],[2,4]]

Solution().maxBuilding(n, restrictions)