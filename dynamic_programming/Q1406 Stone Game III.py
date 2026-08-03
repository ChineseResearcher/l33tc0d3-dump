# dp - hard
from typing import List
from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        # key ideas:
        # 1) same spirit as Stone Game I, just need to adjust the
        # picking rules for the curr. player
        # 2) since picking now only starts from left, we only need to track
        # one index, denoting subproblem concerning stoneValue[i:]
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        @cache
        def f(i: int, turn: int) -> int:

            if i == n: return 0

            res = float('-inf') if turn == 0 else float('inf')

            pfSum = 0
            for j in range(i, i + 3):
                if j == n: break
                pfSum += stoneValue[j]
                # Alice's optimal move: maximise
                if turn == 0:
                    res = fmax(res, pfSum + f(j + 1, 1 - turn))
                # Bob's turn: deduct from net gain + minimise
                else:
                    res = fmin(res, -pfSum + f(j + 1, 1 - turn))
                        
            return res

        res = f(0, 0) # net gain
        if res > 0:
            return 'Alice'
        elif res == 0:
            return 'Tie'
        else:
            return 'Bob'

stoneValue = [1,2,3,7]
stoneValue = [1,2,3,-9]
stoneValue = [1,2,3,6]

Solution().stoneGameIII(stoneValue)