# dp - hard
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        # construct 2-D dp arr with 2 x n dimensions
        # first & second row each represents the case if 
        # we are allowed up to 1 & 2 transactions respectively
        dp = [ [0] * n for _ in range(2)]

        # handle case of up-to-one transaction
        # note for this case we are essentially trying to find
        # the max(prices[i] - prices[j]) up to index i
        low, high = prices[0], prices[0]
        for i in range(1, n):

            if prices[i] < low:
                low = prices[i]
                high = prices[i]
            else:
                high = max(high, prices[i])

            # op1: take the curr. high-low
            op1 = high-low

            # op2: inherit from prev i-1 res
            op2 = dp[0][i-1]

            dp[0][i] = max(op1, op2)

        # handle case of up-to-two transactions
        for i in range(1, n):

            # op1: simply inherit from up-to-one case
            op1 = dp[0][i]

            # op2: making the second transaction after
            # considering prices up to prices[i-1]
            op2 = prices[i] - prices[i-1] + max(dp[0][i-1], dp[1][i-1])

            dp[1][i] = max(op1, op2)

        # find the ans. as the max val in the up-to-two cases
        return max(dp[1])
    
prices = [3,3,5,0,0,3,1,4]
prices = [0,5,0,1,0,10]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [0,3,1,5]
prices = [6,1,3,2,4,7]

Solution().maxProfit(prices)
