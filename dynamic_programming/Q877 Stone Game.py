# dp - medium
from typing import List
from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n = len(piles)
        # key ideas:
        # 1) if we use a recursive DP to determine if subgame (i, j) can be
        # won by Alice if played optimally, the optimal recurrence depends on
        # the recursive states themselves, which is then a loop and not feasible

        # 2) we transform the problem into the checking if Alice
        # can win the game denoted by (0, n-1) given that Bob will also want to maximise
        # his score at each turn

        # 3) we could represent the result of Alice winning by tracking the net
        # gain Alice has Bob at any subgames
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        @cache
        def f(i: int, j: int) -> int:

            if i > j: return 0

            # determine whose turn by remaining length
            turn = (j - i) % 2

            # Alice's optimal move: maximise
            if turn == 1:
                return fmax(piles[i] + f(i + 1, j), piles[j] + f(i, j - 1))
            # Bob's turn: deduct from net gain + minimise
            else:
                return fmin(-piles[i] + f(i + 1, j), -piles[j] + f(i, j - 1))

        return f(0, n - 1) > 0 # net gain > 0 

piles = [5,3,4,5]
piles = [3,7,2,3]

Solution().stoneGame(piles)