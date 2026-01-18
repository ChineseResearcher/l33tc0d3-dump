# prefix sum - medium
from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        # build horizontal and vertical prefix sums
        h_pf = [ [] for _ in range(m) ]
        v_pf = [ [] for _ in range(n) ]

        for r in range(m):
            h_pf[r].append(grid[r][0])
            for c in range(1, n):
                h_pf[r].append(h_pf[r][-1] + grid[r][c])

        for c in range(n):
            v_pf[c].append(grid[0][c])
            for r in range(1, m):
                v_pf[c].append(v_pf[c][-1] + grid[r][c])

        # given some side length, check if there exists 
        # a magic square of this size in the grid
        def checker(l:int) -> bool:

            # fixing a top-left corner (r,c)
            for r in range(m-l+1):
                for c in range(n-l+1):
                    
                    # init. targetSum to north-east diagonal sum
                    targetSum = sum([grid[r+l-1-i][c+i] for i in range(l)])
                    # check south-east diagonal sum
                    if sum([grid[r+i][c+i] for i in range(l)]) != targetSum:
                        continue

                    rowPass = True
                    for i in range(r,r+l):
                        rSum = h_pf[i][c+l-1] - (h_pf[i][c-1] if c-1 >= 0 else 0)
                        if rSum != targetSum:
                            rowPass = False
                            break
                    if not rowPass: continue

                    colPass = True
                    for j in range(c,c+l):
                        cSum = v_pf[j][r+l-1] - (v_pf[j][r-1] if r-1 >= 0 else 0)
                        if cSum != targetSum:
                            colPass = False
                            break
                    if not colPass: continue

                    # otherwise, we found a valid magic square that passes
                    # all checks on the directional sums
                    return True
                
            return False

        ans = 1
        # iterate all possible side length of a square
        for l in range(2, min(m, n)+1):
            if checker(l):
                ans = l

        return ans
    
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]

Solution().largestMagicSquare(grid)