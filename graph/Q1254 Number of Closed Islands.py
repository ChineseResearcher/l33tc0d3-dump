# graph - medium
from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) island(s) that are completely surrounded by water will not have edge cells
        # 2) make use of the property in (1) to determine the answer

        v, ans = set(), 0
        for r0 in range(m):
            for c0 in range(n):
                if grid[r0][c0] == 0 and (r0, c0) not in v:
                    v.add((r0, c0))
                    q, isClosed = deque([(r0, c0)]), True
                    while q:
                        r, c = q.popleft()
                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            isClosed = False
                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 0 and (nr, nc) not in v:
                                    q.append((nr, nc))
                                    v.add((nr, nc))
                    if isClosed: ans += 1

        return ans

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]

Solution().closedIsland(grid)