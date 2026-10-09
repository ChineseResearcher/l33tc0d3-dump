# dp - hard
from functools import cache
class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:

        # key ideas:
        # 1) to meet the constraint that adjacent absolute diff. does
        # not exceed k, simply track the prev. digit

        @cache
        def f(pos: int, tight: bool, pd: int) -> int:

            if pos == N:
                return 1 if pd != -1 else 0

            limit = int(S[pos]) if tight else 9

            res = 0
            for d in range(limit + 1):
                # we have yet to pick any digits
                if pd == -1:
                    res += f(pos + 1,
                            tight and (d == limit),
                            d if d > 0 else -1
                        )
                    
                elif abs(d - pd) <= k:
                    res += f(pos + 1,
                            tight and (d == limit),
                            d)

            return res

        S = str(l - 1)
        N = len(S)
        p1 = f(0, True, -1)

        f.cache_clear()

        S  = str(r)
        N = len(S)
        p2 = f(0, True, -1)

        return p2 - p1

l, r, k = 10, 15, 1
l, r, k = 15, 147, 7
l, r, k = 201, 204, 2

Solution().goodIntegers(l, r, k)