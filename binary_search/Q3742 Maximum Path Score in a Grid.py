# dp - medium
from typing import List
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) bottom-up DP is needed because constraint is too tight
        # 2) 3D table where the innermost layer maps the states of acc. costs from 0 to k 
        # 3) optimisation of k: it does not matter beyond (m+n)
        k = min(k, m + n)

        dp = [ [ [float('-inf')] * (k+1) for _ in range(n) ] for _ in range(m) ]
        if grid[0][0] > 0:
            dp[0][0][1] = grid[0][0]
        else:
            dp[0][0][0] = 0

        for r in range(m):
            for c in range(n):

                if (r,c) == (0,0):
                    continue
                
                v = grid[r][c]
                cost = 1 if v > 0 else 0

                # inherit from left
                if c - 1 >= 0:
                    
                    ub = r + (c - 1) + 1
                    for g in range(min(ub, k)+1):
                        if dp[r][c-1][g] > float('-inf') and g + cost <= k:
                            dp[r][c][g+cost] = fmax(dp[r][c][g+cost], v + dp[r][c-1][g])

                # inherit from top
                if r - 1 >= 0:

                    ub = (r - 1) + c + 1
                    for g in range(min(ub, k)+1):
                        if dp[r-1][c][g] > float('-inf') and g + cost <= k:
                            dp[r][c][g+cost] = fmax(dp[r][c][g+cost], v + dp[r-1][c][g])

        res = max(dp[-1][-1])
        return res if res > float('-inf') else -1
    
grid, k = [[0,1],[2,0]], 1
grid, k = [[0,1],[1,2]], 1

Solution().maxPathScore(grid, k)

