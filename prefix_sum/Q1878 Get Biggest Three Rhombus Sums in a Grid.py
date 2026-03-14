# prefix sum - medium
from typing import List
from collections import defaultdict
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) pre-compute the prefix sums of diagonals (pointing north-east) and 
        # anti-diagonals (poiting south-east), hashed by row / col relationships

        # 2) explore all possible side lengths, and traverse through the grid 
        # to compute the rhombus sum of all valid rhombuses

        main_diag_pf = defaultdict(list)
        for c in range(n):
            for r in range(m):

                pf_sum = 0
                if main_diag_pf[r+c]:
                    pf_sum = main_diag_pf[r+c][-1]

                main_diag_pf[r+c].append(pf_sum + grid[r][c])

        anti_diag_pf = defaultdict(list)
        for r in range(m):
            for c in range(n):

                pf_sum = 0
                if anti_diag_pf[r-c]:
                    pf_sum = anti_diag_pf[r-c][-1]

                anti_diag_pf[r-c].append(pf_sum + grid[r][c])

        # helper to determine offset used for prefix sum indexing
        def find_offset(r:int, c:int, dir:str) -> int:
            if dir == 'main':
                return max(r + c - (m - 1), 0)
            else:
                return max(0 - (r - c), 0)

        # side length explored determined by min(m, n)
        k = min(m, n) // 2 + 1

        # record all rhombus sums in a list
        # note: we record all length-1 rhombus first
        rs = [grid[r][c] for r in range(m) for c in range(n)]
        for l in range(2, k+1):
            # iterate through the top-edges
            for r in range(m):
                for c in range(n):

                    d = l - 1
                    isValid, cornerSum = True, 0
                    # first determine if the implied rhombus is valid
                    for nr, nc in [(r,c), (r+d, c+d), (r+2*d, c), (r+d, c-d)]:
                        if not (0 <= nr < m) or not (0 <= nc < n):
                            isValid = False
                            break
                        cornerSum += grid[nr][nc]

                    if not isValid: continue

                    pf_sum = 0
                    # find the two MAIN diagonal prefix sums
                    # 1) top corner 2) right corner
                    for nr, nc in [(r, c), (r+d, c+d)]:
                        i = nc - find_offset(nr, nc, 'main')
                        pi = i - l
                        pf_sum += main_diag_pf[nr+nc][i] - (main_diag_pf[nr+nc][pi] if pi >= 0 else 0)

                    # find the two ANTI diagonal prefix sums
                    # 1) right corner 2) bottom corner
                    for nr, nc in [(r+d, c+d), (r+2*d, c)]:
                        i = nc - find_offset(nr, nc, 'anti')
                        pi = i - l
                        pf_sum += anti_diag_pf[nr-nc][i] - (anti_diag_pf[nr-nc][pi] if pi >= 0 else 0)

                    rs.append(pf_sum - cornerSum)

        # sort the sums and return largest (distinct) 3 (if any)
        return sorted(set(rs), reverse=True)[:3]

grid = [[7,7,7]]
grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

Solution().getBiggestThree(grid)