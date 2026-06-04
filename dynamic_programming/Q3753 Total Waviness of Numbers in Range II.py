# dp - hard
from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        @cache
        def f(pos: int, tight: bool, pd1: int, pd2: int) -> int:
            
            if pos == N:
                return 0

            limit = int(S[pos]) if tight else 9

            res = 0
            for d in range(limit + 1):
                new_tight = tight and (d == limit)
                if pd1 == -1:
                    if d == 0:
                        res += f(pos + 1, new_tight, pd1, pd2)
                    else:
                        res += f(pos + 1, new_tight, d, pd1)
                
                elif pd2 == -1:
                    res += f(pos + 1, new_tight, d, pd1)

                else:
                    # evaluate peak / valley starting from the 3rd valid digit
                    # (1) check if pd1 can be a local peak
                    isPeak = (pd1 > pd2) and (pd1 > d)
                    # (2) check if pd1 can be a local valley
                    isValley = (pd1 < pd2) and (pd1 < d)

                    # if pd1 is indeed a peak / valley, we need to find out
                    # the count of all possible combinations of numbers of fixing
                    # up to curr. position, as the multiplier
                    if new_tight:
                        rem = S[pos+1:]
                        p = int(rem) + 1 if rem else 1
                    else:
                        rem = (N - pos - 1) * '9'
                        p = int(rem) + 1 if rem else 1
                    res += (isPeak + isValley) * p 
                    
                    res += f(pos + 1, new_tight, d, pd1)

            return res

        S = str(num1-1)
        N = len(S)
        p1 = f(0, True, -1, -1)

        f.cache_clear()

        S = str(num2)
        N = len(S)
        p2 = f(0, True, -1, -1)

        return p2 - p1

num1, num2 = 120, 130
num1, num2 = 198, 202
num1, num2 = 4848, 4848
num1, num2 = int(1e14), int(1e15) # constraint

Solution().totalWaviness(num1, num2)