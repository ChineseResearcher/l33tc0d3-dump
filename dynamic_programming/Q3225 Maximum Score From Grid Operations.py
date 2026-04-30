# dp - hard
from typing import List
from functools import cache
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        prefix = [ [0] * (n+1) for _ in range(n) ]

        for i in range(n):
            sm = 0
            for j in range(n):
                sm += grid[j][i]
                prefix[i][j+1] = sm

        # flag is True when the (i-2)-th col is larger than (i-1)-th col
        @cache
        def f(col, prev_h, flag):

            if col == n:
                return 0

            res = 0 
            for curr_h in range(0, n + 1):

                if prev_h > curr_h:
                    sm = prefix[col][prev_h] - prefix[col][curr_h]
                    res = max(res, sm + f(col + 1, curr_h, True))
                else: 
                    if not flag:
                        sm_prev = prefix[col-1][curr_h] - prefix[col-1][prev_h]
                        res = max(res, sm_prev + f(col + 1, curr_h, False))
                    else:
                        res = max(res, f(col + 1, curr_h, False))

            return res 
        
        return f(0, 0, True)
    
grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Solution().maximumScore(grid)