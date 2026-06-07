# dp - hard
from functools import cache
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        
        S = str(n)
        N = len(S)
        # key ideas:
        # 1) a mask is used to determine if a digit is repeated
        # 2) count suffix variations when a repeated digit is detected 

        @cache
        def f(pos:int, tight:bool, mask:int) -> int:

            if pos == N:
                return 0
            
            limit = int(S[pos]) if tight else 9
            res = 0
            for d in range(limit + 1):
                new_tight = tight and (d == limit)

                # repeated digit
                if mask > 0 and mask & (1 << d):
                    if new_tight:
                        rem = S[pos+1:]
                        p = int(rem) + 1 if rem else 1
                    else:
                        rem = (N - pos - 1) * '9'
                        p = int(rem) + 1 if rem else 1

                    res += p
                    continue

                if mask == 0:
                    new_mask = 0 if d == 0 else mask | (1 << d)
                else:
                    new_mask = mask | (1 << d)

                res += f(pos + 1, new_tight, new_mask)

            return res

        return f(0, True, 0)
    
n = 20
n = 100
n = 1000
n = int(1e9) # constraint

Solution().numDupDigitsAtMostN(n)