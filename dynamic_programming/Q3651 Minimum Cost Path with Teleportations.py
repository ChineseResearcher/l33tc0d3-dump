# dp - hard
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        fmin = lambda a, b : a if a < b else b
        # key ideas:
        # 1) solve for each k incrementally, from 0 to k where 0
        # indicates no teleport available, making it a vanilla matrix dp problem

        # 2) deal w/ two DP tables dp_t & dp_matrix, gets overridden for each k solved
        # dp_t: suffix min. of dp_matrix over distinct grid values
        # dp_matrix: for the curr. k, min. cost to reach each (i, j) cell

        # 3) coordinate compression trick:
        # store distinct grid values in sorted order, then create a map that 
        # maps the indices to distinct values

        dval = set()
        # get distinct values and sort
        for r in range(m):
            for c in range(n):
                dval.add(grid[r][c])

        dval = sorted(list(dval))
        map = {val:idx for idx, val in enumerate(dval)}

        dp_matrix = [ [float('inf')] * n for _ in range(m) ]
        dp_matrix[0][0] = 0

        # helper for solving a grid where only normal move is allowed
        def normal_solve(dp_matrix: List[List[int]]) -> List[List[int]]:
            for r in range(m):
                for c in range(n):
                    if c-1 >= 0:
                        dp_matrix[r][c] = fmin(dp_matrix[r][c], 
                                            grid[r][c] + dp_matrix[r][c-1])
                    if r-1 >= 0:
                        dp_matrix[r][c] = fmin(dp_matrix[r][c], 
                                            grid[r][c] + dp_matrix[r-1][c])
            return dp_matrix

        # solve for no-teleport case first
        dp_matrix = normal_solve(dp_matrix)
                    
        ans = dp_matrix[-1][-1]
        # solve for each teleport incrementally in range [1...k]
        for _ in range(k):

            dp_t = [float('inf')] * len(map)
            # new dp_matrix
            n_dp_matrix = [ [float('inf')] * n for _ in range(m) ]

            # populate dp_t using previous dp_matrix
            for r in range(m):
                for c in range(n):
                    dp_t[map[grid[r][c]]] = fmin(dp_t[map[grid[r][c]]], dp_matrix[r][c])

            # perform suffix min. transformation over dp_t
            for i in range(len(map)-2, -1, -1):
                dp_t[i] = fmin(dp_t[i], dp_t[i+1])

            # assume we use exactly 1 teleportation and reflect it in the new dp_matrix
            for r in range(m):
                for c in range(n):
                    # choose between no-teleport or teleport (knapsack)
                    n_dp_matrix[r][c] = fmin(dp_matrix[r][c], dp_t[map[grid[r][c]]])

            # overlay with normal solve again, so as to improve the cost to (normally) reach
            # some cell (i, j) after (i-1, j) or (i, j-1) has been improved using teleport
            dp_matrix = normal_solve(n_dp_matrix)
            ans = fmin(ans, dp_matrix[-1][-1])

        return ans

grid, k = [[1,3,3],[2,5,4],[4,3,5]], 2
grid, k = [[1,2],[2,3],[3,4]], 1
grid, k = [[3,1],[10,4]], 7
grid, k = [ [1] * 80 for _ in range(80) ], 10 # constraint

Solution().minCost(grid, k)