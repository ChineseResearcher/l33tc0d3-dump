# dp - hard
from functools import cache
class Solution:
    def countFancy(self, l: int, r: int) -> int:

        def isGood(x:int) -> bool:
            xs = str(x)
            n = len(xs)

            # test for ASC
            isAsc = True
            for i in range(1, n):
                if xs[i] <= xs[i-1]:
                    isAsc = False
                    break

            # test for DESC
            isDesc = True
            for i in range(1, n):
                if xs[i] >= xs[i-1]:
                    isDesc = False
                    break
            
            return (isAsc or isDesc)
        
        @cache
        def f(pos:int, tight:bool, pd:int, isAsc:bool, isDesc:bool, dSum:int) -> int:

            if pos == N:
                return 1 if (isAsc or isDesc or isGood(dSum)) else 0
            
            limit = int(S[pos]) if tight else 9
            
            res = 0
            for d in range(limit + 1):
                # pd = -1 indicates that sequence has not started
                if pd == -1:
                    new_pd = -1 if d == 0 else d
                else:
                    new_pd = d

                res += f(pos + 1,
                        tight and (d == limit),
                        new_pd,
                        isAsc and (pd == -1 or d > pd),
                        isDesc and (pd == -1 or d < pd),
                        dSum + d)
                
            return res

        S = str(l-1)
        N = len(S)

        res_l = f(0, True, -1, True, True, 0)

        f.cache_clear()

        S = str(r)
        N = len(S)

        res_r = f(0, True, -1, True, True, 0)

        return res_r - res_l
    
l, r = 8, 10
l, r = 13, 135
l, r = 12340, 12341
l, r = 123456788, 123456788
l, r = int(1e14), int(1e15) # constraint

Solution().countFancy(l, r)