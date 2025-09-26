# dp - hard
from typing import List
from functools import cache
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
    
        wp = dict()
        for w, l, p in prices:
            wp[(w, l)] = p

        @cache
        def recursive_cut(width, length):
            
            res = 0
            # pair-wise distinct wood found
            # i.e. there's no more than 1 wood of the same dim. of diff prices
            if (width, length) in wp:
                res = wp[(width, length)]

            # horizontal cut
            for r in range(1, width // 2 + 1):
                res = max(res, recursive_cut(r, length) + recursive_cut(width-r, length))

            # vertical cut
            for c in range(1, length // 2 + 1):
                res = max(res, recursive_cut(width, c) + recursive_cut(width, length-c))

            return res

        return recursive_cut(m, n)
    
m, n, prices = 3, 5, [[1,4,2],[2,2,7],[2,1,3]]
m, n, prices = 4, 6, [[3,2,10],[1,4,2],[4,1,3]]
m, n, prices = 4, 2, [[4,1,18],[4,2,5],[1,1,20],[3,1,21]]
# constraint
m, n, prices = 200, 200, [[1,1,2],[2,2,1]]

Solution().sellingWood(m, n, prices)