# array - medium
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # we store the rows/cols that should be set to 0
        zero_row, zero_col = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)

        # set zeroes in-place
        for r in zero_row:
            for c in range(n):
                matrix[r][c] = 0

        for c in zero_col:
            for r in range(m):
                matrix[r][c] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

Solution().setZeroes(matrix)