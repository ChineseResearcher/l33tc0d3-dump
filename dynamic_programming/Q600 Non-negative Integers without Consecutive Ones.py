# dp - hard
from functools import cache
class Solution:
    def findIntegers(self, n: int) -> int:

        # key ideas:
        # 1) if we perform digit DP on base-10 number itself it would TLE because
        # n could be as large as 1e9, so we perform digit DP in base-2 format

        # 2) recursive recurrence depends not only on tight bound, but
        # also on whether previous bit was already set or not

        # digits in binary form: either 0 or 1
        digits = list(map(int, bin(n)[2:]))
        N = len(digits)

        @cache
        def f(pos: int, tight: bool, prevBit: int) -> int:

            if pos == N:
                return 1
            
            res = 0
            ub = digits[pos] if tight else 1
            for d in range(ub + 1):
                # additional constraint on upper bound if prevBit is already set
                if prevBit == 1 and d > 0:
                    break

                res += f(pos+1, tight and (d == ub), d)

            return res

        return f(0, True, 0)

n = 5
n = int(1e9)

Solution().findIntegers(n)