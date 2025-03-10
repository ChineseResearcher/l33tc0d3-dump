# graph - medium
from collections import deque
class Solution:
    def numEnclaves(self, grid):
        
        m, n = len(grid), len(grid[0])
        # we could perform multisource BFS from any land cells
        # that sit on the boundary, and land cells that are left
        # unvisited are simply land cells that are part of enclaves

        multisource = set()
        for c in range(n):
            if grid[0][c] == 1 and (0, c) not in multisource:
                multisource.add((0, c))
            if grid[m-1][c] == 1 and (m-1, c) not in multisource:
                multisource.add((m-1, c))

        for r in range(m):
            if grid[r][0] == 1 and (r, 0) not in multisource:
                multisource.add((r, 0))
            if grid[r][n-1] == 1 and (r, n-1) not in multisource:
                multisource.add((r, n-1))

        # inherit multisource as the visited set
        bfs_queue = deque(multisource)
        while bfs_queue:

            r, c = bfs_queue.popleft()
            # explore cardinal directions
            if c-1 >= 0 and (r, c-1) not in multisource and grid[r][c-1] == 1:
                bfs_queue.append((r, c-1))
                multisource.add((r, c-1))

            if c+1 < n and (r, c+1) not in multisource and grid[r][c+1] == 1:
                bfs_queue.append((r, c+1))
                multisource.add((r, c+1))

            if r-1 >= 0 and (r-1, c) not in multisource and grid[r-1][c] == 1:
                bfs_queue.append((r-1, c))
                multisource.add((r-1, c))

            if r+1 < m and (r+1, c) not in multisource and grid[r+1][c] == 1:
                bfs_queue.append((r+1, c))
                multisource.add((r+1, c))

        # increment when we encounter an unvisited land cell
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in multisource:
                    ans += 1

        return ans
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
grid = [[1,0,1],[0,1,0],[1,0,1]]
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

Solution().numEnclaves(grid)