# simulation - medium
class Solution:
    def coloredCells(self, n: int) -> int:
        # it is observed that the number of blue cells can be considered
        # as the sum of row cells:
        # for n = 2, # of cells = 1 + 3 + 1 = 5
        # for n = 3, # of cells = 1 + 3 + 5 + 3 + 1 = 13
        # for n = 4, # of cells = 1 + 3 + 5 + 7 + 5 + 3 + 1 = 25

        # the middle row at n = k would have # of cells = 1 + 2 * (k-1)
        middle_row = 1 + 2 * (n-1)

        ans = middle_row
        # the remaining rows are all symmetric about the middle row
        for row_cnt in range(middle_row-2, 0, -2):
            ans += 2 * row_cnt

        return ans
    
n = 4

Solution().coloredCells(n)