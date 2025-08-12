# dp - medium
from functools import cache
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        MOD = int(1e9 + 7)

        @cache
        def recursive_sum(target, startInt):

            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            if pow(startInt, x) > target:
                return 0
            
            skip = recursive_sum(target, startInt+1)
            take = recursive_sum(target-pow(startInt, x), startInt+1)
            curr_res = (skip + take) % MOD

            return curr_res % MOD

        return recursive_sum(n, 1)
    
n, x = 10, 2
n, x = 4, 1
n, x = 300, 1 # constraints

Solution().numberOfWays(n, x)