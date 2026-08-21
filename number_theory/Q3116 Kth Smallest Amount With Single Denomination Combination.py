# number theory - hard
import math
from typing import List
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) binary search on range [1, maxC * k]
        # 2) validate curr. candidate coin by counting all possible coin(s)
        # smaller or equal to curr., by checking against a set of base denominations

        coins.sort()
        maxC = coins[-1] # for binary search right bound

        # we reduce original denominations to a set that pairwise co-primes
        base_denom = []
        for i in range(n):
            curr = coins[i]

            isMultiple = False
            for j in range(i):
                if curr % coins[j] == 0:
                    isMultiple = True
                    break

            if not isMultiple:
                base_denom.append(curr)

        # helper for finding Lowest Common Multiple for a pair
        def lcm(a:int, b:int) -> int:
            return a // math.gcd(a, b) * b

        # define a helper to compute the count of possible coin sums <= target
        def countCoinSum(T:int, denom:List[int]) -> int:
            n = len(denom)
            # by applying inclusion-exclusion formula, we can determine
            # for any subsets of denom, the count of coin sums it contributes
            # to the total count of coin sums <= T

            res = 0
            # enumerate all possible subsets of denom
            for mask in range(1, 1 << n):
                L, b = 1, 0
                for i in range(n):
                    if mask & (1 << i):
                        b += 1
                        L = lcm(L, denom[i])
                        if L > T: break

                # curr. subset have a LCM that is larger than T, thus invalid
                if L > T: continue

                # depending on the parity of the size of the subset,
                # we either add or subtract from the count result
                if b % 2 == 1:
                    res += T // L
                else:
                    res -= T // L

            return res

        l, r = 1, maxC * k
        ans = r
        while l <= r:

            mid = (l + r) >> 1
            # let y denote the count of coin sums
            y = countCoinSum(mid, base_denom)

            if y < k:
                l = mid + 1
            else:
                r = mid - 1
                ans = fmin(ans, mid)

        return ans

coins, k = [5,2], 7
coins, k = [3,6,9], 3

Solution().findKthSmallest(coins, k)