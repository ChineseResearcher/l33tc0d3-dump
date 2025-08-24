# array - medium
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])

        # imagine we are always traversing from bottom-left to top-right diagonally
        # and for a diagonal we keep going until either row or col goes out boundary

        # list down all the bottom-left starting points
        sp = [(r, 0) for r in range(m-1)] + [(m-1, 0)] + [(m-1, c) for c in range(1, n)]

        ans, reverse = [], False
        for br, bc in sp:

            curr_diag = []
            cr, cc = br, bc
            while 0 <= cr < m and 0 <= cc < n:
                curr_diag.append(mat[cr][cc])
                # move north-east
                cr -= 1
                cc += 1

            if reverse:
                curr_diag = curr_diag[::-1]

            ans.extend(curr_diag)
            reverse = not reverse

        return ans 
    
mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2],[3,4]]

Solution().findDiagonalOrder(mat)