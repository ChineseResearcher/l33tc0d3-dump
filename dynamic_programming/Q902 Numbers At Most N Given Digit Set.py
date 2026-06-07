# dp - hard
from typing import List
from functools import cache
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        S = str(n)
        N = len(S)

        # key ideas:
        # 1) standard digit DP but with only select digits available
        # 2) conditionally prepend "0" to digits to allow preceding 0s

        digits = [int(x) for x in digits]

        @cache
        def f(pos:int, tight: bool, started: bool) -> int:

            if pos == N:
                return 1 if started else 0
            
            limit = int(S[pos]) if tight else 9

            res = 0
            avail = [0] + digits if not started else digits
            for d in avail:  
                if d > limit:
                    break
                
                new_started = started or (d > 0)
                res += f(pos + 1, tight and (d == limit), new_started)

            return res

        return f(0, True, False)

digits, n = ["7"], 8
digits, n = ["1","3","5","7"], 100
digits, n = ["1","4","9"], 1000000000

Solution().atMostNGivenDigitSet(digits, n)