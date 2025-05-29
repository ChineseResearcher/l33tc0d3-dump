# prefix sum - medium
from typing import List
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # treat this as a prefix sum problem rather than dp
        # compute prefix sum for each row & col
        rpf = [ [0] * n for _ in range(m) ]
        for r in range(m):

            rsum = 0
            for c in range(n):
                rsum += grid[r][c]
                rpf[r][c] = rsum

        cpf = [ [0] * m for _ in range(n) ]
        for c in range(n):

            csum = 0
            for r in range(m):
                csum += grid[r][c]
                cpf[c][r] += csum

        ans = 0
        for r in range(m):
            for c in range(n):

                # we only care about cells w/ val = 1
                if grid[r][c] == 0:
                    continue
                
                ans = max(ans, 1)
                # determine the furthest diagonal by looking at
                # the row-wise and col-wise cells leading up to (r,c)
                delta1 = 0
                for i in range(c, -1, -1):
                    if grid[r][i] == 0:
                        break
                    delta1 = c-i

                delta2 = 0
                for j in range(r, -1, -1):
                    if grid[j][c] == 0:
                        break
                    delta2 = r-j

                diag = min(delta1, delta2)
                if diag == 0:
                    continue

                while diag > 0:
                    
                    # shrink our diagonal until we find the first valid subgrid
                    nr, nc = r-diag, c-diag
                    
                    side_len = c - nc + 1 # or r - nr + 1
                    rsum = rpf[nr][c] - rpf[nr][nc-1] if nc > 0 else rpf[nr][c]
                    csum = cpf[nc][r] - cpf[nc][nr-1] if nr > 0 else cpf[nc][r]
        
                    if rsum == csum == side_len:
                        ans = max(ans, side_len ** 2)
                        break

                    diag -= 1

        return ans
    
grid = [[1,1,1],[1,0,1],[1,1,1]]
grid = [[1,1,0,0]]

Solution().largest1BorderedSquare(grid)