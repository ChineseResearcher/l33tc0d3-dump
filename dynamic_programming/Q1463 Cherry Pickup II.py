# dp - hard
from functools import cache
from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        fmax = lambda a, b: a if a > b else b
        delta = [(1,-1), (1,0), (1,1)]
        # key ideas:
        # 1) represent each sub-problem using the coordinate of the two robots
        # 2) we only need three states (r, c1, c2), where (r, c1) refers to first
        # robot and (r, c2) refers to second robot

        @cache
        def f(r:int, c1:int, c2:int) -> int:

            if r == m-1:
                return 0
            
            res = 0
            # there will be up to 3 x 3 combinations of next move
            for dr, dc in delta:
                nr, nc1 = r + dr, c1 + dc

                if 0 <= nc1 < n:
                    for _, dc in delta:
                        nc2 = c2 + dc

                        if 0 <= nc2 < n:
                            # both land on same cell
                            if nc1 == nc2:
                                res = fmax(res, grid[nr][nc1] + \
                                                f(nr, nc1, nc2))
                            # land on different cells
                            else:
                                res = fmax(res, grid[nr][nc1] + grid[nr][nc2] + \
                                                f(nr, nc1, nc2))
                                
            return res

        return f(0, 0, n-1) + grid[0][0] + grid[0][n-1]

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# constraint
grid = [ [1] * 70 for _ in range(70) ] 

Solution().cherryPickup(grid)