# recursion - hard
import math
from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:

        v, h = destination
        # key ideas:
        # 1) recursion + combinatorics (to prune recursion)
        # 2) why terminate at k = 1?
        # because when we look for the smallest (k = 1) instruction given 
        # some "v", "h", the ongoing sequence is counted as 1 occurrence,
        # thus we construct "h"(s) + "v"(s) to satisfy the smallest order

        def f(h:int, v:int, k:int) -> str:

            if k == 1:
                return h * 'H' + v * 'V'

            # compute suffix combinations
            g = math.comb(h + v - 1, h - 1)
            
            # if we make a horizontal move ('h' reduced by 1)
            # there is no change to the k-th lexicographical order we want to locate
            if k <= g:
                return 'H' + f(h - 1, v, k)
            # if we make a vertical move, we need to account for
            # the number of possible combinations skipped if 'h' (if any) was placed
            else:
                return 'V' + f(h, v - 1, k - g)

        return f(h, v, k)

destination, k = [2,3], 2
destination, k = [2,3], 3
destination, k = [1,1], 1
destination, k = [3,0], 1
destination, k = [0,3], 1

Solution().kthSmallestPath(destination, k)