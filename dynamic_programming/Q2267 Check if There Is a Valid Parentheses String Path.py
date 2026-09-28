# dp - hard
from functools import cache
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) top-down DP with 3 states (r, c, k) where k refers to the accumulated
        # number of unclosed left brackets in its path
        # 2) prune recursion based on current position & max. number of possible
        # right brackets remaining
        # 3) observe that any path length sums up to m + n - 1, and if this is odd,
        # we can confirm the answer if false as there is always 1 left bracket unmatched
        if (m + n - 1) % 2: return False 

        @cache
        def f(r: int, c: int, k: int) -> bool:

            if r == m - 1 and c == n - 1:
                return True if k == 1 and grid[r][c] == ')' else False

            # prune (1): insufficient right brackets
            if k > m - r + n - c:
                return False

            # prune (2): right brackets before left brackets
            if k < 0:
                return False

            nk = k + 1 if grid[r][c] == '(' else k - 1
            if r + 1 < m and f(r + 1, c, nk):
                return True

            if c + 1 < n and f(r, c + 1, nk):
                return True

            return False

        return f(0, 0, 0)

grid = [[")",")"],["(","("]]
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]

Solution().hasValidPath(grid)