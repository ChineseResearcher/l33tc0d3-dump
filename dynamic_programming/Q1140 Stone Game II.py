# dp - medium
from typing import List
from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        # key ideas:
        # 1) one key feature of this problem is that, if a player picks k piles
        # at curr. round, the other player can pick up to 2 * k piles in the next round
        # 2) maximise Alice total stone count by exploring all possible k with DP
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        @cache
        def f(i:int, M:int, alice_turn:bool) -> int:

            if i >= n: return 0
            L = min(i + 2 * M, n) # farthest reachable pile

            res = 0 if alice_turn else float('inf')
            prefixSum = 0
            for j in range(i, L):
                prefixSum += piles[j]

                nres = f(j + 1, fmax(j - i + 1, M), not alice_turn)
                if alice_turn:
                    res = fmax(res, prefixSum + nres)
                else:
                    res = fmin(res, nres)

            return res

        return f(0, 1, True)

piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]

Solution().stoneGameII(piles)