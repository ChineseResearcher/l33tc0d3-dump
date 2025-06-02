# graph - hard
from typing import List
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # this question is labelled hard because there's a trick to
        # achieving a disconnected state (i.e. >= 2 islands) no matter
        # how big m & n is. That is, given m x n map filled all w/ 1s (worst case?)
        # we just need to choose one corner and isolate the corner land cell
        # w/ at most two operations to turn neighbouring land cells into water

        # so if the grid given is already disconnected, return 0
        # if it can be disconnected by turning only 1 land cell to 0, return 1
        # otherwise, return 2!

        # given that m & n is at max 30, implying that O((m * n) ^ 2) is efficient
        # we can first test for return-0 case followed by return-1 case
        m, n = len(grid), len(grid[0])

        offsets = [(1,0),(-1,0),(0,1),(0,-1)]

        def isDisconnected(grid):

            visited = set()
            def dfs(r, c):

                visited.add((r,c))

                for dx, dy in offsets:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and \
                        grid[nr][nc] == 1 and (nr, nc) not in visited:
                        dfs(nr, nc)

            islandCnt = 0
            for r in range(m):
                for c in range(n):

                    if grid[r][c] == 1 and (r,c) not in visited:
                        if islandCnt > 0:
                            return True

                        _ = dfs(r, c)
                        islandCnt += 1

            return False if islandCnt == 1 else True

        # 1) return-0 case
        if isDisconnected(grid):
            return 0

        # 2) return-1 case
        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:
                    # try flipping this
                    grid[r][c] = 0
                    if isDisconnected(grid):
                        return 1
                    grid[r][c] = 1 # backtrack

        # otherwise, return 2
        return 2
    
grid = [[0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]]

grid = [[1,1]]

grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]

Solution().minDays(grid)