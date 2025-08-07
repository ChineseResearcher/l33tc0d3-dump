# dp - medium
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        # we can always make amount 0 by choosing no coins
        dp[0] = 1

        # it does not work if we swap the relative order
        # of the for-loops, and it honestly is very abstract 
        # for me to understand why must we enforce coins iteration outside
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
            
        return dp[-1]
    
amount, coins = 5, [1,2,5]
amount, coins = 3, [2]
amount, coins = 10, [10]
amount, coins = 5, [1,2,5]

Solution().change(amount, coins)