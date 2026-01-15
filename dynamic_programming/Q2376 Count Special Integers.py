# dp - hard
from functools import cache
class Solution:
    def countSpecialNumbers(self, n: int) -> int:

        digits = list(map(int, str(n)))
        N = len(digits)

        @cache
        def f(pos:int, tight:bool, bitmask:int) -> int:

            if pos == N:
                return 1
            
            ub = digits[pos] if tight else 9

            res = 0
            for d in range(ub + 1):
                # pick an unused digit by checking against bitmask
                if bitmask & (1 << d) == 0:

                    n_bitmask = bitmask
                    if d == 0:
                        # only mark usage of digit 0 if the seq. has started
                        if n_bitmask > 0:
                            n_bitmask |= (1 << d)
                    else:
                        n_bitmask |= (1 << d)

                    res += f(pos+1, tight and (d == ub), n_bitmask)

            return res

        # minus 1 to discount n = 0
        return f(0, True, 0) - 1
    
n = 5
n = 20
n = 135
n = 2 * int(1e9)

Solution().countSpecialNumbers(n)