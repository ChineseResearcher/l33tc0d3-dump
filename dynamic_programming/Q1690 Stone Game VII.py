# dp - hard
from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        n = len(stones)
        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) pre-process prefix sums so as to obtain range sum [l, r] quickly
        # 2) alternate max / min objectives for Alice / Bob respectively

        pfSum = [stones[0]]
        for i in range(1, n):
            pfSum.append(pfSum[-1] + stones[i])

        dp = [ [-1] * n for _ in range(n) ]

        def f(l:int, r:int) -> int:
            
            turn = (n - (r - l + 1)) % 2
            if l == r:
                return 0

            if dp[l][r] != -1: return dp[l][r]
            # rangeSum / subproblem result if leftmost is removed
            s1, f1 = pfSum[r] - pfSum[l], f(l + 1, r)
            # rangeSum / subproblem result if rightmost is removed
            s2, f2 = pfSum[r - 1] - (pfSum[l - 1] if l - 1 >= 0 else 0), f(l, r - 1)

            if turn == 0:
                res = fmax(s1 + f1, s2 + f2)
            else:
                res = fmin(-s1 + f1, -s2 + f2)

            dp[l][r] = res
            return res

        return f(0, n - 1)

stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

Solution().stoneGameVII(stones)