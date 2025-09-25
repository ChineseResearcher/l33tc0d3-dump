# graph - medium
from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        # global visited
        visited = set()

        delta = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(sr, sc):

            # given a source cell ('O') that is unvisited,
            # perform BFS to reach connected '0's and store the processed cells
            q = deque([(sr, sc)])
            visited.add((sr, sc))

            processed, onEdge = [], False
            while q:

                r, c = q.popleft()
                # boundary cell: invalidate whole region
                if r in [0, m-1] or c in [0, n-1]:
                    onEdge = True
                processed.append((r, c))

                for dr, dc in delta:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and \
                    board[nr][nc] == 'O' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return processed if not onEdge else []

        # res. arr store the cells that can be captured
        res = []
        for r in range(m):
            for c in range(n):

                if board[r][c] == 'O' and (r, c) not in visited:
                    res.extend(bfs(r, c))

        for r, c in res:
            board[r][c] = 'X'

        for x in board:
            print(x)

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]

board = [
    ["X","O","O","X","X","X","O","X","O","O"],
    ["X","O","X","X","X","X","X","X","X","X"],
    ["X","X","X","X","O","X","X","X","X","X"],
    ["X","O","X","X","X","O","X","X","X","O"],
    ["O","X","X","X","O","X","O","X","O","X"],
    ["X","X","O","X","X","O","O","X","X","X"],
    ["O","X","X","O","O","X","O","X","X","O"],
    ["O","X","X","X","X","X","O","X","X","X"],
    ["X","O","O","X","X","O","X","X","O","O"],
    ["X","X","X","O","O","X","O","X","X","O"]
    ]

Solution().solve(board)