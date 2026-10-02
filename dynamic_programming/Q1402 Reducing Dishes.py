# dp - hard
from functools import cache
class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        n = len(satisfaction)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) sorting + greedy + DP
        # 2) greedily place the larger numbers at the back to allow time coefficient
        # to accumulate before reaching it, so as to maximise our result
        satisfaction.sort()

        @cache
        def f(i: int, t: int) -> int:
            if i == n:
                return 0

            res = float('-inf')
            # knapsack decisions
            # skip curr. dish
            res = fmax(res, f(i + 1, t))
            # take (cook) curr. dish
            res = fmax(res, t * satisfaction[i] + f(i + 1, t + 1))

            return res

        return f(0, 1)

satisfaction = [4,3,2]
satisfaction = [-1,-4,-5]
satisfaction = [-1,-8,0,5,-9]

Solution().maxSatisfaction(satisfaction)