# binary search - hard
from collections import deque
from typing import List
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        # key ideas:
        # 1) since all land cells will be eventually covered with water,
        # we can use binary search to find the last (max.) day on which it allows
        # traversal from the top to the bottom

        # 2) binary search O(log(n*m)) with BFS O(n*m) for n*m <= 2*1e4

        # define bfs helper
        def bfs(lastDay:int) -> bool:

            if lastDay == 0:
                return True

            # define water cells as a set
            waterCell = set([(cells[i][0]-1, cells[i][1]-1) for i in range(lastDay)])

            q, visited = deque(), set()
            # multi-source enqueue top-row land cells
            for c in range(col):
                if (0,c) not in waterCell:
                    q.append((0, c))
                    visited.add((0, c))

            while q:

                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col \
                        and (nr, nc) not in waterCell and (nr, nc) not in visited:
                        if nr == row - 1: # reached bottom
                            return True
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return False

        l, r = 0, row * col
        while l <= r:

            mid = (l + r) // 2
            if bfs(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r

row, col, cells = 2, 1, [[1,1],[2,1]]
row, col, cells = 2, 2, [[1,1],[2,1],[1,2],[2,2]]
row, col, cells = 2, 2, [[1,1],[1,2],[2,1],[2,2]]
row, col, cells = 3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

Solution().latestDayToCross(row, col, cells)