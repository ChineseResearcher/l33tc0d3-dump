# dp - medium
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        # init. dp arr. of length n, storing max. profit 
        # to the subproblem concerning up to prices[:i]
        dp = [0] * n

        for i in range(1, n):

            # op1: if today's price is larger than yesterday
            # we add on to the max. profit accrued at i-1
            if prices[i] > prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]

            # op2: otherwise, we just inherit the max. profit at i-1
            else:
                dp[i] = dp[i-1]

        return dp[-1]
    
prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

Solution().maxProfit(prices)