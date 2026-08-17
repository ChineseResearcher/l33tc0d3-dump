# dp - hard
from typing import List
from functools import cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)
        # key ideas:
        # 1) partition DP w/ Max objective
        # 2）O(n^3) is acceptable for this Qn

        # pre-compute prefix sum
        pfSum = [stoneValue[0]]
        for i in range(1, n):
            pfSum.append(stoneValue[i] + pfSum[-1])

        fmax = lambda a, b: a if a > b else b

        @cache
        def f(l:int, r:int) -> int:

            if l == r: return 0

            # rangeSum for [l...r]
            rangeSum = pfSum[r] - (pfSum[l - 1] if l - 1 >= 0 else 0)

            # track prefix sum as the left sum
            res, lSum = 0, 0
            for p in range(l, r):
                lSum += stoneValue[p]
                rSum = rangeSum - lSum

                if lSum < rSum:
                    res = fmax(res, lSum + f(l, p))
                elif lSum > rSum:
                    res = fmax(res, rSum + f(p + 1, r))
                # Alice decides when both sums tie
                else:
                    res = fmax(res, lSum + fmax(f(l, p), f(p + 1, r)))

            return res

        return f(0, n - 1)

stoneValue = [6,2,3,4,5,5]
stoneValue = [7,7,7,7,7,7,7]
stoneValue = [10,9,8,7,6,5,4,3,2,1]

Solution().stoneGameV(stoneValue)