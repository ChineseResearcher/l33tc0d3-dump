# dp - medium
from typing import List
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        n = len(prices)
        # key ideas:
        # 1) track prefix max. for both long / short pos. for each transaction cap [1...k]
        # 2) with prefix max. tracked we could achieve O(n * k * 2), note that k is 
        # multiplied by 2 because we break down 1 transaction into open / close
        dp = [ [[0] * 2 for _ in range(n) ] for _ in range(2 * k) ]

        # 0: long pos, 1: short pos
        pf_max = [ [[float('-inf')] * 2 for _ in range(n) ] for _ in range(2 * k) ]

        fmax = lambda a, b: a if a >= b else b

        # note that the optimal answer might result from
        # a strategy involving < k trades, and < n prices
        ans = float('-inf')
        for i in range(n):
            for j in range(2 * k):

                # only 1 trade per day, so up to day i
                # there's maximally j trades done
                if j > i:
                    break 

                for trade in [0, 1]:
                    
                    # there's previous open / close
                    prevMaxLong, prevMaxShort = 0, 0
                    if j - 1 >= 0 and i - 1 >= 0:
                        prevMaxLong, prevMaxShort = pf_max[j-1][i-1][0], pf_max[j-1][i-1][1]

                    # to open a new position
                    if j % 2 == 0:
                        dp[j][i][trade] = fmax(prevMaxLong, prevMaxShort) + \
                                        (-prices[i] if trade == 0 else prices[i])
                    
                    # to close an opened position
                    else:
                        if trade == 0:
                            dp[j][i][trade] = prevMaxLong + prices[i]
                        else:
                            dp[j][i][trade] = prevMaxShort - prices[i]

                        # track best solution
                        ans = fmax(ans, dp[j][i][trade])

                    # update prefix max.
                    pf_max[j][i][trade] = fmax(pf_max[j][i-1][trade], dp[j][i][trade])

        return ans
    
prices, k = [1,7,9,8,2], 2
prices, k = [12,16,19,19,8,1,19,13,9], 3
prices, k = [6,11,1,5,3,15,8], 3

Solution().maximumProfit(prices, k)