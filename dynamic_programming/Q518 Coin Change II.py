# dp - medium
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp[i] stores the number of ways to sum the coins to amount = i
        dp = [0] * (amount + 1)
        # always possible to just not choose any coins and obtain a sum of 0
        dp[0] = 1

        for coin in coins:
            for coinSum in range(coin, amount + 1):

                # why the transition is correct ?
                # when dp[coinSum] is inheriting from dp[coinSum - coin]
                # where the result stored for dp[coinSum - coin] was based on
                # using all coin(s) up to and EXcluding the curr. coin as the denomination set
                # why this matters ?
                # this successfully avoids counting the duplicates 
                # that would show up if we compute DP using the below swapped loops instead:

                # for coinSum in range(amount + 1):
                # ----for coin in coins:
                # --------if coinSum >= coin:
                # ------------dp[coinSum] += dp[coinSum - coin]

                # if we let coins = [1,2,4], amount = 5
                # the correct dp arr:   [1,1,2,2,4,4]
                # the incorrect dp arr: [1,1,2,3,6,10] (we can see duplicates inflation)
                # note: 4 ways to use coinSet [1,2,4] to obtain 5 are:
                # [1,1,1,1,1], [1,1,1,2], [1,2,2], [1,4] 
                dp[coinSum] += dp[coinSum - coin]

        return dp[-1]
    
amount, coins = 3, [2]
amount, coins = 10, [10]
amount, coins = 5, [1,2,5]
amount, coins = 5, [1,2,4]

Solution().change(amount, coins)