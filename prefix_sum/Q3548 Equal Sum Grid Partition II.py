# prefix sum - hard
from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) borrow the logic from part I to solve for undiscounted scenario
        # 2) solve for discounted scenarios row-wise and col-wise

        # build row / col prefix sums
        row_pf, col_pf = [0] * m, [0] * n

        TOTAL, pr, pc = 0, -1, -1
        for r in range(m):
            for c in range(n):
                TOTAL += grid[r][c]
                if c > pc:
                    row_pf[r] += grid[r][c]

                if r > pr:
                    col_pf[c] += grid[r][c]

                pc = c
                if c == n-1:
                    pr += 1
                    pc = -1

        rSum = 0
        for x in row_pf:
            rSum += x
            if rSum == TOTAL - rSum:
                return True
            
        rSum = 0
        for x in col_pf:
            rSum += x
            if rSum == TOTAL - rSum:
                return True
            
        # explore discounting
        # handle special case: m = 1 or n = 1
        if n == 1:
            def row_wise_discount(start:int, end:int, step:int) -> bool:
                pf_sum = 0
                for r in range(start, end, step):
                    pf_sum += row_pf[r]
                    diff = pf_sum - (TOTAL - pf_sum)
                    if diff > 0 and diff in [row_pf[r], row_pf[start]]:
                        return True
                return False
            if row_wise_discount(0, m-1, 1):
                return True
            if row_wise_discount(m-1, 0, -1):
                return True

        elif m == 1:
            def col_wise_discount(start:int, end:int, step:int) -> bool:
                pf_sum = 0
                for c in range(start, end, step):
                    pf_sum += col_pf[c]
                    diff = pf_sum - (TOTAL - pf_sum)
                    if diff > 0 and diff in [col_pf[c], col_pf[start]]:
                        return True
                return False
            if col_wise_discount(0, n-1, 1):
                return True
            if col_wise_discount(n-1, 0, -1):
                return True

        # m > 1 and n > 1
        else:
            def row_wise_discount(start:int, end:int, step:int) -> bool:
                pf_sum, seen, onhold = 0, set(), set()

                release_idx = start + 1 if end > start else start - 1
                for r in range(start, end, step):

                    pf_sum += row_pf[r]
                    # add curr. elements to seen
                    for c in range(n):
                        # when in starting row, middle elements are
                        # put onhold and added later
                        if r == start and 0 < c < n-1:
                            onhold.add(grid[r][c])
                            continue
                        seen.add(grid[r][c])

                    if r == release_idx: seen |= onhold

                    diff = pf_sum - (TOTAL - pf_sum)
                    if diff > 0 and diff in seen:
                        return True
                    
                return False

            def col_wise_discount(start:int, end:int, step:int) -> bool:
                pf_sum, seen, onhold = 0, set(), set()
                release_idx = start + 1 if end > start else start - 1
                for c in range(start, end, step):
                    pf_sum += col_pf[c]
                    for r in range(m):
                        if c == start and 0 < r < m-1:
                            onhold.add(grid[r][c])
                            continue
                        seen.add(grid[r][c])
                    if c == release_idx: seen |= onhold
                    diff = pf_sum - (TOTAL - pf_sum)
                    if diff > 0 and diff in seen:
                        return True
                return False

            # scan row-wise top to bottom
            if row_wise_discount(0, m-1, 1):
                return True
            # scan row-wise bottom to top
            if row_wise_discount(m-1, 0, -1):
                return True

            # scan col-wise from left to right
            if col_wise_discount(0, n-1, 1):
                return True
            # scan col-wise from right to left
            if col_wise_discount(n-1, 0, -1):
                return True

        return False
    
grid = [[1,4],[2,3]]
grid = [[1,2],[3,4]]
grid = [[1],[1],[1],[4],[1]]
grid = [[100000],[86218],[100000]]

Solution().canPartitionGrid(grid)