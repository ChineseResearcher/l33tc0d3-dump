# graph - medium
from collections import deque
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) normal BFS traversal and track island sum
        
        v, ans = set(), 0
        for r0 in range(m):
            for c0 in range(n):
                if grid[r0][c0] > 0 and (r0, c0) not in v:
                    q, s = deque([(r0, c0)]), 0
                    v.add((r0, c0))
                    while q:
                        r, c = q.popleft()
                        s += grid[r][c]
                        s %= k
                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] > 0 and (nr, nc) not in v:
                                    q.append((nr, nc))
                                    v.add((nr, nc))
                    if s % k == 0:
                        ans += 1

        return ans

grid, k = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], 3
grid, k = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], 5

Solution().countIslands(grid, k)