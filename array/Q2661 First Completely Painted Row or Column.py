# array - medium
class Solution:
    def firstCompleteIndex(self, arr, mat) -> int:
        m, n = len(mat), len(mat[0])

        # since all values in matrix are unique, first store the the coords
        # corresponding to each unique val. in a dict
        coord = dict()
        for r in range(m):
            for c in range(n):

                coord[mat[r][c]] = (r, c)

        # initiate two dict to store the number of painted elements in each row/col
        row_painted, col_painted = {i:0 for i in range(m)}, {i:0 for i in range(n)}

        for idx, element in enumerate(arr):
            row, col = coord[element]
            row_painted[row] += 1
            col_painted[col] += 1

            if row_painted[row] == n or col_painted[col] == m:
                return idx

arr, mat = [1,3,4,2], [[1,4],[2,3]]
arr, mat = [2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]

Solution().firstCompleteIndex(arr, mat)