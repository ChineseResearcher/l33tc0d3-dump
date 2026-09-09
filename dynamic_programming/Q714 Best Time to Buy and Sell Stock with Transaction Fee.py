# dp - medium
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) two linear DP tables denoting maxProfit if hold / no-hold on day i
        # 2) map transitions amongst two tables:
        # hold -> no-hold: add sell price to profit
        # no-hold to hold: subtract buy price + transaction fee from profit
        hold, not_hold = [-(prices[0] + fee)], [0]

        for i in range(1, n):
            p = prices[i]
            not_hold.append(fmax(not_hold[-1],
                                 p + hold[-1])
                                 )
            hold.append(fmax(not_hold[-2] - p - fee,
                             hold[-1])
                             )

        # max. profit achieved after last complete transaction
        return not_hold[-1]

prices, fee = [1,3,2,8,4,9], 2
prices, fee = [1,3,7,5,10,3], 3

Solution().maxProfit(prices, fee)