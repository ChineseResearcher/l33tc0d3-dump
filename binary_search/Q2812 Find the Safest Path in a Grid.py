# binary search - medium
from collections import deque
from typing import List, Tuple
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)
        # key ideas:
        # 1) use multisource-BFS to pre-compute the min. manhattan dist.
        # of every empty cell to a thief cell
        # 2) binary search on the answer, and test each target with BFS

        thief = []
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    thief.append((r,c))

        def multisource_BFS(sources: List[Tuple[int]]) -> List[List[int]]:
            # TC: O(V+E) = O(n^2)
            dist = [[float('inf')] * n for _ in range(n)]

            q = deque()
            for r, c in sources:
                dist[r][c] = 0
                q.append((0, r, c))

            while q:
                d, r, c = q.popleft()

                if d > dist[r][c]:
                    continue

                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        nd = d + 1
                        if nd < dist[nr][nc]:
                            dist[nr][nc] = nd
                            q.append((nd, nr, nc))

            return dist

        distToThief = multisource_BFS(thief)

        def canReach(targetMin: int) -> bool:

            # test if we can reach (n-1, n-1) starting (0, 0)
            # with all cells in path having distToThief >= targetMin
            if distToThief[0][0] < targetMin: return False

            q, v = deque([(0,0)]), set(((0,0),))
            while q:
                r, c = q.popleft()
                if r == n-1 and c == n-1:
                    return True
                
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if (nr, nc) not in v:
                            if grid[nr][nc] == 0:
                                if distToThief[nr][nc] >= targetMin:
                                    q.append((nr, nc))
                                    v.add((nr, nc))

            return False

        l, r, ans = 0, n-1, 0
        while l <= r:

            mid = (l + r) >> 1
            if canReach(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans

grid = [[1,0,0],[0,0,0],[0,0,1]]
grid = [[0,0,1],[0,0,0],[0,0,0]]
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
grid = [[1] * 400 for _ in range(400)] # constraint

Solution().maximumSafenessFactor(grid)