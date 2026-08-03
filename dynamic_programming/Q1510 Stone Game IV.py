# dp - hard
S = set([pow(i, 2) for i in range(1, int(int(1e5) ** 0.5) + 1)])
from functools import cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        # key ideas:
        # 1) for each subproblem dp[k], if k is already a squared number,
        # we can terminate the game and decide the winner
        # 2) otherwise, explore all squared numbers < k, with early termination
        # if result is deterministic

        @cache
        def f(k:int, turn:int) -> bool:

            if k in S: return True if turn == 0 else False

            aliceWin = False if turn == 0 else True
            # iterate from largest smaller squared number for speed
            for g in range(int(k ** 0.5), 0, -1):
                nres = f(k - pow(g, 2), 1 - turn)
                # Alice's turn: only one win scenario is needed to affirm win
                if turn == 0:
                    aliceWin |= nres
                    if aliceWin: return True 

                # Bob's turn: only one loss scenario is needed to reject win
                else:
                    aliceWin &= nres
                    if not aliceWin: return False

            return aliceWin

        return f(n, 0)

n = 1
n = 2
n = 4

Solution().winnerSquareGame(n)