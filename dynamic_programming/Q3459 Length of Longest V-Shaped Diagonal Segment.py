# dp - hard
from typing import List
from functools import cache
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        # store the offsets in diagonal directions
        offset = [(-1,1), (1,1), (1,-1), (-1,-1)]

        @cache
        def recursive_build(r, c, dir, turned):

            curr_val = grid[r][c]

            curr_res = 1
            # travel in the same direction
            nr, nc = r + offset[dir][0], c + offset[dir][1]
            if 0 <= nr < m and 0 <= nc < n and abs(curr_val - grid[nr][nc]) == 2:
                curr_res = 1 + recursive_build(nr, nc, dir, turned)

            if not turned:

                # 90 deg clockwise
                dr, dc = offset[(dir+1+4) % 4]
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and abs(curr_val - grid[nr][nc]) == 2:
                    curr_res = max(curr_res, 1 + recursive_build(nr, nc, (dir+1+4) % 4, True))

            return curr_res

        ans = 0
        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:
                    
                    ans = max(ans, 1)
                    for dir, (dr, dc) in enumerate(offset):
                        sr, sc = r + dr, c + dc
                        if 0 <= sr < m and 0 <= sc < n and grid[sr][sc] == 2:
                            ans = max(ans, 1 + recursive_build(sr, sc, dir, False))

        return ans
    
grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
grid = [[1,1,1,2,0,0],[0,0,0,0,1,2]]

Solution().lenOfVDiagonal(grid)