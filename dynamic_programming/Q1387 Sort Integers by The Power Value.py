# dp - medium
from functools import cache
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        # key ideas:
        # 1) cache results for each solved x
        # 2) iterate [lo, hi] and store each (power, val) in an array and sort

        @cache
        def f(x:int) -> int:
            if x == 1: return 0
            if x % 2 == 0:
                return 1 + f(x // 2)
            else:
                return 1 + f(3 * x + 1)
        
        res = []
        for x in range(lo, hi+1):
            res.append((f(x), x))
        res.sort()

        return res[k-1][1]

lo, hi, k = 12, 15, 2
lo, hi, k = 7, 11, 4
lo, hi, k = 1, 1000, 1000 # constraint

Solution().getKth(lo, hi, k)