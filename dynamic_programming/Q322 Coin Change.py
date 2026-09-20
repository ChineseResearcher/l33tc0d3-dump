# dp - medium
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) for some amount "a", it is possible to form "a-c" first
        # and achieve "a" with an additional coin
        # 2) the fewest coins needed to form "a-c" is stored in dp[a - c]
        dp = [float('inf')] * (amount + 1)

        # 0 dollar with no coins
        dp[0] = 0

        all_coins = sorted(set(coins))
        for a in range(1, amount + 1):
            for c in all_coins:
                if c > a: break
                dp[a] = fmin(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] < float('inf') else -1
    
coins, amount = [2], 3
coins, amount = [1], 0
coins, amount = [1,2,5], 11
coins, amount = [156,265,40,280], 9109

Solution().coinChange(coins, amount)