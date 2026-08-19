# dp - hard
from typing import List
from functools import cache
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        n = len(stones)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) pick / skip strategy with result sign change depending on which player
        # 2) pre-process prefix sum on the stones array

        pfSum = [stones[0]]
        for i in range(1, n):
            pfSum.append(pfSum[-1] + stones[i])

        @cache
        def f(i:int, turn:int) -> int:

            # 0: Alice's turn, 1: Bob's turn
            if i == n - 1:
                rSum = pfSum[-1]
                return rSum if turn == 0 else -rSum

            skip = f(i + 1, turn)
            pick = f(i + 1, 1 - turn)
            if turn == 0:
                return fmax(skip, pfSum[i] + pick)
            else:
                return fmin(skip, -pfSum[i] + pick)

        # must have started from the 2nd stone for Alice's 1st turn
        return f(1, 0)

stones = [-10,-12]
stones = [-1,2,-3,4,-5]
stones = [7,-6,5,10,5,-2,-6]

Solution().stoneGameVIII(stones)