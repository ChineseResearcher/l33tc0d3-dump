# graph - hard
from collections import deque, defaultdict
from typing import List
class UnionFind:
    def __init__(self, n):
        # Initialize the Union-Find structure with n elements
        self.parent = list(range(n))  
        self.rank = [1] * n           

    def find(self, x):
        # Find with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        # first simulate the grid after hits are turned "0"s
        grid2 = [row[:] for row in grid]
        for r, c in hits:
            grid2[r][c] = 0

        dsu = UnionFind(m * n)
        stable = [False] * (m * n)
        cnt = defaultdict(int)

        # helper to map (r,c) onto linear index
        k = lambda r, c: r * n + c

        visited = set()
        # use a bfs process to make each island union-ed and
        # mark stable status if applicable
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r,c) not in visited:

                    # (r,c) is the master node of this island
                    parent = k(r, c)

                    q = deque([(r,c)])
                    visited.add((r, c))
                    islandStable = True if r == 0 else False
                    currCnt = 0

                    while q:

                        xr, xc = q.popleft()
                        currCnt += 1

                        dsu.parent[k(xr, xc)] = parent
                        stable[k(xr, xc)] = islandStable

                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = xr + dr, xc + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid2[nr][nc] == 1:
                                    if (nr, nc) not in visited:
                                        q.append((nr, nc))
                                        visited.add((nr, nc))

                    cnt[parent] = currCnt

        # process the hits backwards, and find out the number of
        # blocks that would fall as a result of the i-th hit
        ans = []
        for r, c in hits[::-1]:

            if grid[r][c] == 0:
                ans.append(0)
                continue

            # boolean to track if (r,c) or any neighbour is already stable
            is_stable = (r == 0)
            # number of all blocks involved
            agg_cnt = 1
            # number of unstable blocks
            unstab_cnt = 0

            valid_cells = []
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc

                # filter only neighbour 1-cell
                if nr >= m or nr < 0 or nc >= n or nc < 0:
                    continue
                if grid2[nr][nc] != 1:
                    continue

                valid_cells.append((nr, nc))

            # to derive agg_cnt and unstab_cnt
            # note: we need count from unique parents
            seen = set()
            for nr, nc in valid_cells:
                dsu.find(k(nr, nc))
                np = dsu.parent[k(nr, nc)]
                if stable[np]:
                    is_stable = True
                else:
                    if np not in seen:
                        unstab_cnt += cnt[np]
                if np not in seen:
                    agg_cnt += cnt[np]
                seen.add(np)

            for nr, nc in valid_cells:
                # union neighbours
                dsu.union(k(r,c), k(nr, nc))
                dsu.find(k(r, c))
                dsu.find(k(nr, nc))

            cnt[dsu.parent[k(r,c)]] = agg_cnt
            stable[dsu.parent[k(r,c)]] = is_stable

            if is_stable:
                ans.append(unstab_cnt)
            else:
                ans.append(0)

            # back-fill grid2
            grid2[r][c] = 1

        return ans[::-1]

grid, hits = [[1,0,0,0],[1,1,1,0]], [[1,0]]
grid, hits = [[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]
grid, hits = [[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]]
grid, hits = [[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]]
grid, hits = [[1,0,1],[0,0,1]], [[1,0],[0,0]]

Solution().hitBricks(grid, hits)