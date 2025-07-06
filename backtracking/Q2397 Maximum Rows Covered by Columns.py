# backtracking - medium
from typing import List
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:

        m, n = len(matrix), len(matrix[0])
        # first we do binary-encoding for each row
        row_enc = {r:0 for r in range(m)}

        for r in range(m):
            for c in range(n-1, -1, -1):

                bit_idx = n - c - 1
                if matrix[r][c] == 1:
                    row_enc[r] |= (1 << bit_idx)

        # write a backtracking function that generate
        # all combinations of selecting "numSelect" cols
        self.ans = 0
        def backtrack(idx, c_enc, bits):

            # confirmed max. cols selected
            if bits == numSelect:
                curr_ans = 0
                for _, r_enc in row_enc.items():
                    if r_enc == 0 or (r_enc & ~c_enc) == 0:
                        curr_ans += 1

                self.ans = max(self.ans, curr_ans)

            for i in range(idx, n):
                # early stop for insufficient cols left to pick numSelect cols
                if n - i < numSelect - bits:
                    break

                c_enc |= (1 << i)
                backtrack(i+1, c_enc, bits+1)
                # backtrack
                c_enc &= ~(1 << i)

        _ = backtrack(0, 0, 0)
        return self.ans
    
matrix, numSelect = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 2
matrix, numSelect = [[1],[0]], 1

Solution().maximumRows(matrix, numSelect)