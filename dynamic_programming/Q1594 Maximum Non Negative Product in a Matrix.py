# dp - medium
from functools import cache
from typing import List, Tuple
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        @cache
        def f(r: int, c: int) -> Tuple[int, int]:

            if (r, c) == (m-1, n-1):
                return (grid[r][c], grid[r][c])
            
            if grid[r][c] == 0:
                return (0,0)
            
            res0, res1 = float('-inf'), float('inf')
            for dr, dc in [(0,1), (1,0)]:
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    nres0, nres1 = f(nr, nc)
                    res0 = fmax(res0, nres0)
                    res1 = fmin(res1, nres1)
            
            if grid[r][c] > 0:
                return (grid[r][c] * res0, grid[r][c] * res1)
            else:
                return (grid[r][c] * res1, grid[r][c] * res0)
            
        ans, _ = f(0, 0)
        return ans % int(1e9+7) if ans >= 0 else -1

grid = [[1,3],[0,-4]]
grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
grid = [[-1,-4,2],[4,3,-1],[2,-4,4],[1,-1,-4]]

Solution().maxProductPath(grid)