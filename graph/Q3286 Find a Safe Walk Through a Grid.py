# graph - medium
import heapq
from typing import List
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) to arrive at certain cell (r, c) in the grid, we need to
        # construct the path with the minimum cost to health
        # 2) we could then frame this as a Djikstra's application except that
        # now instead of tracking of min. dist, we track the max. health
        # attaintable by reaching a cell in the grid

        if grid[0][0] == 1: health -= 1
        # if health == 0: return False

        maxHealth = [[0] * n for _ in range(m)]
        maxHealth[0][0] = health

        maxHeap = [(-health, 0, 0)]
        while maxHeap:

            h, r, c = heapq.heappop(maxHeap)
            h = abs(h)
            if h > maxHealth[r][c]:
                continue

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]
                    if nh > maxHealth[nr][nc]:
                        heapq.heappush(maxHeap, (-nh, nr, nc))
                        maxHealth[nr][nc] = nh

        return maxHealth[-1][-1] > 0

grid, health = [[1,1,1],[1,0,1],[1,1,1]], 5
grid, health = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1
grid, health = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3

Solution().findSafeWalk(grid, health)