# dp - medium
from functools import cache
class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def solve(a, b):

            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1
            
            if b <= 0:
                return 0

            curr_res = 0
            # op1: get 100 ml from A, 0 ml from B
            curr_res += 0.25 * solve(a-100, b)

            # op2: 75 ml from A, 25 ml from B
            curr_res += 0.25 * solve(a-75, b-25)

            # op3: 50 ml from A, 50 ml from B
            curr_res += 0.25 * solve(a-50, b-50)

            # op4: 25 ml from A, 75 ml from B
            curr_res += 0.25 * solve(a-25, b-75)

            return curr_res

        # a crucial optimisation in here is recognising that 
        # as n -> inf, answer approaches 1, since the answer
        # can be 1e-5 within the actual answer, for n >= 5000
        # we can safely just return 1
        return solve(n, n) if n < 5000 else 1
    
n = 50
n = 100
n = 4999

Solution().soupServings(n)