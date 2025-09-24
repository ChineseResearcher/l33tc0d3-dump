# dp - medium
from typing import List
from functools import cache
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        @cache
        def recursive_cut(r1, c1, r2, c2):

            # (r1, c1) as the bottom-left coord
            # (r2, c2) as the top-right coord
            
            # if sub-region is a 1x1 block, exit
            if c2 == c1 + 1 and r1 == r2 + 1:
                return 0

            res = float('inf')
            # optimisation: find the most expensive cut 
            # in both horizontal and vertical directions and prune

            # horizontal cut
            max_h_cut, max_r = 0, None
            for r in range(r2, r1-1):
                if horizontalCut[r] > max_h_cut:
                    max_h_cut, max_r = horizontalCut[r], r
            
            if max_h_cut > 0:
                res = min(res, max_h_cut + 
                               recursive_cut(max_r+1, c1, r2, c2) +
                               recursive_cut(r1, c1, max_r+1, c2))
            
            # vertical cut
            max_v_cut, max_c = 0, None
            for c in range(c1, c2-1):
                if verticalCut[c] > max_v_cut:
                    max_v_cut, max_c = verticalCut[c], c

            if max_v_cut > 0:
                res = min(res, max_v_cut + 
                               recursive_cut(r1, c1, r2, max_c+1) +
                               recursive_cut(r1, max_c+1, r2, c2))
            
            return res

        return recursive_cut(m, 0, 0, n)
    
m, n, horizontalCut, verticalCut = 3, 2, [1,3], [5]
m, n, horizontalCut, verticalCut = 2, 2, [7], [4]
m, n, horizontalCut, verticalCut = 6, 3, [2,3,2,3,1], [1,2]
# constraint
import random
m, n, horizontalCut, verticalCut = 20, 20, [random.randint(1, 1000) for _ in range(20)], [random.randint(1, 1000) for _ in range(20)]

Solution().minimumCost(m, n, horizontalCut, verticalCut)