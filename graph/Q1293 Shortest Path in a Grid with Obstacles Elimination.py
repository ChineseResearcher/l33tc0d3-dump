# graph - hard
from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        if m * n == 1: return 0
        # key ideas:
        # 1) use a modified BFS process to track visited states (r, c, k)
        # where k is the number of remaining removals allowed
        # 2) use a nested boolean array to optimize lookup time
        v = [[[False] * (k+1) for _ in range(n)] for _ in range(m)]
        v[0][0][k] = True

        q, ans = deque([(0, 0, k, 0)]), -1
        while q:

            r, c, k, d = q.popleft()
            if r == m-1 and c == n-1:
                ans = d
                break

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # removal exhausted
                    if grid[nr][nc] and not k:
                        continue
                    nk = k-1 if grid[nr][nc] else k
                    # valid candidate
                    if not v[nr][nc][nk]:
                        v[nr][nc][nk] = True
                        q.append((nr, nc, nk, d+1))

        return ans

grid, k = [[0,1,1],[1,1,1],[1,0,0]], 1
grid, k = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1
grid, k = [[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,1],[0,0,0,1,0,0,1,0]], 1

Solution().shortestPath(grid, k)