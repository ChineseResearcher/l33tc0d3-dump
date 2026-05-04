# dp - hard
from functools import cache
class Solution:
    def racecar(self, target: int) -> int:
        
        fmin = lambda a, b: a if a < b else b

        def is_diff_geometric_sum(diff: int):
            """
            Checks if the input diff is a sum of the geometric series 1, 2, 4, 8...
            The sum of this series is always 2^n - 1.
            """
            # If diff = 2^n - 1, then (diff + 1) must be a power of 2.
            # We check if x is a power of 2 using (x & (x - 1) == 0).
            return (diff & (diff + 1)) == 0

        @cache
        def f(pos:int) -> int:

            # our recursive logic ensures that we are always
            # 1) facing right when pos < target
            # 2) facing left when pos > target
            d = abs(pos - target)

            if is_diff_geometric_sum(d):
                # count number of contiguous "A" to reduce diff to 0
                return d.bit_count()
            
            n = d.bit_length()
            # if the distance is not a direct geometric sum, we have
            # TWO move strategies:
            # 1) go past target in n contiguous "A" + "R" OR
            # 2) take n-1 contiguous "A" + "R" + m contiguous of "A" + "R"
            # subject to the condition that m < n-1
            if pos < target:
                
                res = f(pos + pow(2,n) - 1) + n + 1 # op1
                for m in range(n-1):
                    op2 = f(pos + pow(2,n-1) - 1 - (pow(2,m) - 1)) + n - 1 + 1 + m + 1
                    res = fmin(res, op2)

                return res

            elif pos > target:

                res = f(pos - pow(2,n) + 1) + n + 1 # op1
                for m in range(n-1):
                    op2 = f(pos - (pow(2,n-1) - 1) + pow(2,m) - 1) + n - 1 + 1 + m + 1
                    res = fmin(res, op2)

                return res
            
        return f(0)

target = 6
target = 3
target = 4 # "AARRA" -> 0,1,3,3,3,4
target = 5 # "AARARAA" -> 0,1,3,3,2,2,3,5
target = 10000 # constraint

Solution().racecar(target)