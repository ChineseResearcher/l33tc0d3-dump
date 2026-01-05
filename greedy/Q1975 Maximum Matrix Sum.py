# greedy - medium
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        # key ideas:
        # 1) if the count of -ve numbers is even, they can all be inverted to +ve,
        # and if the count is odd, we will be left w/ one that is -ve

        # 2) track the integer of the smallest magnitude, to be used as the kept -ve

        neg_cnt, min_val = 0, float('inf')
        fmin = lambda a,b: a if a < b else b

        gridSum = 0
        for r in range(n):
            for c in range(n):

                min_val = fmin(min_val, abs(matrix[r][c]))

                gridSum += abs(matrix[r][c])
                if matrix[r][c] < 0:
                    neg_cnt += 1

        if neg_cnt % 2 == 0:
            return gridSum
        else:
            return gridSum - 2 * min_val

matrix = [[1,-1],[-1,1]]
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
matrix = [[9,-3,-4],[-4,-1,-3],[-6,-3,-3]]
matrix = [[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]
matrix = [[-1,0,-1],[-2,1,3],[3,2,2]]
matrix = [[2,9,3],[5,4,-4],[1,7,1]]

Solution().maxMatrixSum(matrix)