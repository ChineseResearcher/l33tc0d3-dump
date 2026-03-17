# greedy - medium
from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) scan the matrix row by row, and for each row, track the
        # cumulative heights of contiguous 1-blocks in the vertical directions

        # 2) sort the cumu. heights in desc. order and apply greedy thinking
        # to find the max. submatrice area
        ch = [0] * n

        ans = 0
        for r in range(m):
            # update cumu. heights first
            for c in range(n):
                if matrix[r][c] == 1:
                    ch[c] += 1
                else:
                    ch[c] = 0

            # obtain a sorted version of the curr. heights
            ch_sorted = sorted(ch, reverse=True)

            for c in range(n):
                # bounding height is the curr. iterated height
                bh = ch_sorted[c]
                ans = fmax(ans, bh * (c + 1))

        return ans

matrix = [[1,0,1,0,1]]
matrix = [[1,1,0],[1,0,1]]
matrix = [[0,0,1],[1,1,1],[1,0,1]]

Solution().largestSubmatrix(matrix)