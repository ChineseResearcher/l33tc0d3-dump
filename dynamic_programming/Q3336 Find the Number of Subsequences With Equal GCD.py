# dp - hard
import math
from typing import List
from functools import cache
# pre-compute GCD(a, b) for a, b in range [1, 200]
# O(n*m^2*log(m)) reduced to O(n*m^2)
GCD = [ [0] * 201 for _ in range(201) ]
for a in range(1, 201):
    for b in range(a, 201):
        res = math.gcd(a, b)
        GCD[a][b] = res
        GCD[b][a] = res

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        n = len(nums)
        MOD = int(1e9 + 7)
        # key ideas:
        # 1) take-or-skip DP
        # 2) realise that the GCD of a subset of numbers is non-increasing
        # as we add more numbers to the set, hence the gcd of subsequences 1/2
        # can be simply calculated using the existing gcd(s)

        @cache
        def f(i:int, g1:int, g2:int) -> int:

            if i == n: return 0

            res = 0
            # skip
            res += f(i + 1, g1, g2)

            # take curr. number to either subseq. 1 or 2
            new_g1 = GCD[g1][nums[i]] if g1 != -1 else nums[i]
            res += (1 if new_g1 == g2 else 0) + f(i + 1, new_g1, g2)

            new_g2 = GCD[g2][nums[i]] if g2 != -1 else nums[i]
            res += (1 if new_g2 == g1 else 0) + f(i + 1, g1, new_g2)

            return res % MOD

        return f(0, -1, -1)
    
nums = [1,2,3,4]
nums = [10,20,30]
nums = [200] * 200 # constraint

Solution().subsequencePairCount(nums)