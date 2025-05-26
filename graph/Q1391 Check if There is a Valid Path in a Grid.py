# graph - medium
from typing import List
from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        # there are six linkages type available, denote them as coordinates delta
        delta = {1: [(0, -1), (0, 1)],
                2: [(-1, 0), (1, 0)],
                3: [(0, -1), (1, 0)],
                4: [(0, 1), (1, 0)],
                5: [(0, -1), (-1, 0)],
                6: [(0, 1), (-1, 0)]}

        # also define valid transitions given an offset
        vt = {(0, 1): [1,3,5],
            (0, -1): [1,4,6],
            (1, 0): [2,5,6],
            (-1, 0): [2,3,4]}

        m, n = len(grid), len(grid[0])
        bfs_q, visited = deque([(0,0)]), set(((0,0),))

        while bfs_q:

            r, c = bfs_q.popleft()
            if r == m-1 and c == n-1:
                return True
                
            # obtain the two offsets possible for the value at curr. cell
            offsets = delta[grid[r][c]]

            for dx, dy in offsets:

                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n \
                and (nr, nc) not in visited and grid[nr][nc] in vt[(dx, dy)]:

                    bfs_q.append((nr, nc))
                    visited.add((nr, nc))

        return False
    
grid = [[2,4,3],[6,5,2]]
grid = [[1,2,1],[1,2,1]]
grid = [[1,1,2]]

Solution().hasValidPath(grid)