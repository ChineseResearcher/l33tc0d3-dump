# binary search - medium
from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # first build prefix sum in 2-D fashion
        pfSum = [ [0] * n for _ in range(m) ]
        for i in range(m):

            rSum = 0
            for j in range(n):
                rSum += mat[i][j]
                pfSum[i][j] = rSum + (pfSum[i-1][j] if i > 0 else 0)

        def isValid(sideLen, pfSum):

            # a helper to check if for a square w/ sideLen,
            # is there a subgrid w/ sum <= threshold
            
            # iterate through the top-left vertices of all possible subgrids
            for r in range(m-sideLen+1):
                for c in range(n-sideLen+1):

                    # pfSum in 2-D requires us to first locate the
                    # bottom right vertice of the square
                    subgridSum = pfSum[r+sideLen-1][c+sideLen-1]

                    # if necessary, need to deduct prefixed-subgrids
                    if c > 0:
                        subgridSum -= pfSum[r+sideLen-1][c-1]
                    if r > 0:
                        subgridSum -= pfSum[r-1][c+sideLen-1]
                    # add back the overlapped part that was double-subtracted
                    if r > 0 and c > 0:
                        subgridSum += pfSum[r-1][c-1]

                    if subgridSum <= threshold:
                        return True
                    
            return False

        # apply binary search on the answer itself, bounded between 1 and min(m, n)
        l, r = 1, min(m, n)

        while l <= r:

            sl = (l + r) // 2
            if isValid(sl, pfSum):
                print(sl)
                l = sl + 1
            else:
                r = sl - 1

        # one key note to take is when we want to find max. possible valid number
        # we return "r", and return "l" when we want to find min. possible
        return r
    
mat, threshold = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4
mat, threshold = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1

Solution().maxSideLength(mat, threshold)