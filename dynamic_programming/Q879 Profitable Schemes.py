# dp - hard
from functools import cache
MOD = int(1e9 + 7)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:

        m = len(group)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) knapsack DP with states (t, p, i), where "t" refers to the total
        # man count of curr. scheme, "p" refers to the profit of curr. scheme (capped at minProfit),
        # and "i" indicates we have considered up to the i-th crime

        @cache
        def f(t: int, p: int, i: int) -> int:

            # insufficient manpower
            if t > n: return 0
            
            if i == m:
                return 1 if p == minProfit else 0

            res = 0
            # knapsack transitions:
            # 1) skip curr. crime
            res += f(t, p, i + 1)
            # 2) take curr. crime as part of the scheme
            res += f(t + group[i], fmin(p + profit[i], minProfit), i + 1)

            return res % MOD

        return f(0, 0, 0)

n, minProfit, group, profit = 5, 3, [2,2], [2,3]
n, minProfit, group, profit = 10, 5, [2,3,5], [6,7,8]

Solution().profitableSchemes(n, minProfit, group, profit)