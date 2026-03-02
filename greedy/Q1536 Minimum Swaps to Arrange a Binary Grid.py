# greedy - medium
from typing import List
from collections import Counter
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        # key ideas:
        # 1) if we define the rightmost "1" in every row as the frontier,
        # then after processing all rows, the columns of all frontiers should
        # occupy exactly row 0 to row n-1.

        # 2) to early reject impossible grids we could use a counter dict
        # for each col, and the i-th col would be able to accept up to (i+1)
        # rows w/ frontiers placed at the i-th col

        # 3) to correctly count of the min. number of swaps needed to simulate
        # bubble sort process for each index forward

        col_set, ft_col_order = set(), []
        frontier_cnt = Counter()

        for r in range(n):

            all_zero = True
            for c in range(n-1, -1, -1):

                if grid[r][c] == 1:

                    frontier_cnt[c] += 1
                    col_set.add(c)
                    ft_col_order.append(c)

                    all_zero = False
                    break
            
            if all_zero:
                ft_col_order.append(-1)

        if len(col_set) < n:
            for col, freq in frontier_cnt.items():
                if freq > n-col:
                    return -1

        ans = 0
        # O(n^2) to count swaps 
        # simulation of bubble sorting
        for i in range(n):

            j = i
            # to find the FIRST j in range [i...n-1] s.t. 
            # ft_col_order[j] <= i, this is because for the i-th row,
            # the rightmost "1" should be at or before column i
            while j < n and ft_col_order[j] > i:
                j += 1

            # no valid j
            if j == n:
                return -1

            # imagine we've found such j and we are 
            # bubbling ft_col_order[j] to index i to the left
            ans += j - i
            while j > i:
                ft_col_order[j], ft_col_order[j-1] = ft_col_order[j-1], ft_col_order[j]
                j -= 1

        return ans

grid = [[0,0],[0,1]]
grid = [[1,0,0],[1,1,0],[1,1,1]]
grid = [[0,0,1],[1,1,0],[1,0,0]]
grid = [[0,1,0],[1,1,0],[1,0,0]]
grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
grid = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]

Solution().minSwaps(grid)