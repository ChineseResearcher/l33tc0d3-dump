# array - medium
from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        # observe for a n x n matrix, if we encode r-c as the
        # group_id, then the diagonals from bottom-left triangle, incl. the middle diagonal
        # would have id in range [0, 1, ..., n-1],  whereas the top-right
        # triangle would have diagonals w/ id in range [-1, -2, ..., -(n-1)]

        # use a hashmap to store all diagonal values based on group_id
        diag_vals = {i:[] for i in range(-(n-1), n)}
        for r in range(n):
            for c in range(n):
                diag_vals[r-c].append(grid[r][c])

        for k, l in diag_vals.items():
            if k >= 0:
                diag_vals[k] = sorted(l)
            else:
                diag_vals[k] = sorted(l, reverse=True)

        for r in range(n):
            for c in range(n):
                grid[r][c] = diag_vals[r-c].pop()

        return grid
    
grid = [[1,7,3],[9,8,2],[4,5,6]]
grid = [[0,1],[1,2]]
grid = [[1]]

Solution().sortMatrix(grid)