# graph - hard
from typing import List
from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        m, n = len(grid), len(grid[0])
        # key ideas
        # 1) apply BFS and track (node, keysFound) as states
        # 2) keysFound is a bitmask up to "k" bits

        FULL_KEY = 0
        # first locate the starting pos and also define the
        # all-keys-found mask as we encounter keys
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    r0, c0 = r, c
                if grid[r][c].islower():
                    o = ord(grid[r][c]) - ord('a')
                    FULL_KEY |= (1 << o)

        q = deque([(0, r0, c0, 0)]) # moves, r, c, keysFound
        visited = set([(r0, c0, 0)])

        ans = -1
        while q:

            moves, r, c, keysFound = q.popleft()
            if keysFound == FULL_KEY:
                ans = moves
                break

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                # boundary check
                if 0 <= nr < m and 0 <= nc < n:
                    # skip walls
                    if grid[nr][nc] == '#':
                        continue

                    # skip locks with no corresponding keys
                    if grid[nr][nc].isupper():
                        o = ord(grid[nr][nc]) - ord('A')
                        if not keysFound & (1 << o):
                            continue

                    # define new mask
                    new = keysFound
                    if grid[nr][nc].islower():
                        o = ord(grid[nr][nc]) - ord('a')
                        new |= (1 << o)

                    if (nr, nc, new) not in visited:
                        q.append((moves+1, nr, nc, new))
                        visited.add((nr, nc, new))

        return ans

grid = ["@Aa"]
grid = ["@.a..","###.#","b.A.B"]
grid = ["@..aA","..B#.","....b"]

Solution().shortestPathAllKeys(grid)