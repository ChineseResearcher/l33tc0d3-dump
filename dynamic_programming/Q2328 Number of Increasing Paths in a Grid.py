# dp - hard
from typing import List
from functools import cache
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        offsets = [(0,1),(0,-1),(1,0),(-1,0)]

        MOD = int(1e9+7)

        @cache
        def recursive_visit(r, c):

            # length-1 path
            curr_res = 1
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    curr_res += recursive_visit(nr, nc)
                    curr_res %= MOD

            return curr_res

        ans = 0
        for r in range(m):
            for c in range(n):
                ans += recursive_visit(r, c)
                ans %= MOD 

        return ans
    
grid = [[1,1],[3,4]]
grid = [[1],[2]]
import random
grid = [[random.randint(1, int(1e5)) for _ in range(1000)] for _ in range(1000)] # constraint

Solution().countPaths(grid)