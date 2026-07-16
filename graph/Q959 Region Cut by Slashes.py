# graph - medium
from typing import List
from collections import deque
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        # key ideas:
        # 1) for slashed cells, represent visited states as (r, c, 1/2)
        # where 1/2 corresponds to two states for either diagonal ('d') or anti-diagonal ('ad')
        # 2) pre-define deltas for each possible cell state
        # for example, for diagonals, with the upper section named "1", it can only go
        # north or west.
        # 3) pre-define the section that we will land in given an incoming direction
        # for example, for diagonals, if incoming direction is east, it will land in section 1.

        # record the type of diagonals for slashed cells, otherwise empty
        slashed = [ [''] * n for _ in range(n) ]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    slashed[r][c] = 'ad'
                elif grid[r][c] == "\\":
                    slashed[r][c] = 'd'

        delta = {'': [(0,1),(1,0),(0,-1),(-1,0)],
                'd': {1: [(-1,0),(0,1)], 2: [(0,-1),(1,0)]},
                'ad': {1: [(-1,0),(0,-1)], 2: [(0,1),(1,0)]}}

        landing = {'d': {(0,1): 2, (1,0): 1, (0,-1): 1, (-1,0): 2},
                'ad': {(0,1): 1, (1,0): 1, (0,-1): 2, (-1,0): 2}}

        v = set() # global visited
        def bfs(r0: int, c0: int, s0: int) -> None:

            q = deque([(r0, c0, s0)])
            v.add((r0, c0, s0))

            while q:

                r, c, s = q.popleft()
                shape = slashed[r][c]
                delta_ = delta[shape][s] if shape else delta[shape]

                for dr, dc in delta_:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        # check the shape of neighbour
                        next_shape = slashed[nr][nc]
                        if next_shape:
                            # get the landed section in neighbour
                            ns = landing[next_shape][(dr, dc)]
                        else:
                            # non-slashed neighbour with section defaults to -1
                            ns = -1
                        # enqueue
                        if (nr, nc, ns) not in v:
                            v.add((nr, nc, ns))
                            q.append((nr, nc, ns))

        ans = 0
        for r in range(n):
            for c in range(n):
                shape = slashed[r][c]
                # slashed cell: consider two sections
                if shape:
                    for s in [1, 2]:
                        if (r, c, s) not in v:
                            _ = bfs(r, c, s)
                            ans += 1
                else:
                    if (r, c, -1) not in v:
                        _ = bfs(r, c, -1)
                        ans += 1

        return ans

grid = [" /","/ "]
grid = [" /","  "]
grid = ["/\\","\\/"]

Solution().regionsBySlashes(grid)