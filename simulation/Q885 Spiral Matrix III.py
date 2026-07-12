# simulation - medium
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        T = rows * cols
        # key ideas:
        # 1) simulate the spiral moves, with each arm length +1 after every two turns
        # 2) record the cells that we cross in the order of traversal
        delta = [(0,1), (1,0), (0,-1), (-1,0)]

        r, c, direction, dist = rStart, cStart, 0, 1
        ans = [[r, c]]
        while len(ans) < T:
            
            dr, dc = delta[direction]
            for i in range(1, dist + 1):
                nr, nc = r + i * dr, c + i * dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    ans.append([nr, nc])

            r, c = nr, nc
            direction = (direction + 1) % 4
            if direction in [0, 2]:
                dist += 1

        return ans
    
rows, cols, rStart, cStart = 5, 6, 1, 4
rows, cols, rStart, cStart = 1, 4, 0, 0

Solution().spiralMatrixIII(rows, cols, rStart, cStart)