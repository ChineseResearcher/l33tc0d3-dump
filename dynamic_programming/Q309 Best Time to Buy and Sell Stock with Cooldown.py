# dp - medium
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
    
        # Initialize DP arrays:
        hold = [-float('inf')] * n  # Maximum profit on day i when holding stock
        not_hold = [0] * n  # Maximum profit on day i when not holding stock (after sell or cooldown)
        
        hold[0] = -prices[0]  # If we buy on day 0
        
        for i in range(1, n):
            # Two possibilities for holding stock on day i:
            # 1. We continue holding stock from day i-1.
            # 2. We buy stock on day i (including cooldown of one day so referring to not_hold[i-2])
            hold[i] = max(hold[i-1], not_hold[i-2] - prices[i])
            
            # Two possibilities for not holding stock on day i:
            # 1. We sell the stock on day i (which means hold[i-1] is the profit before selling).
            # 2. We skip and continue not holding
            not_hold[i] = max(hold[i-1] + prices[i], not_hold[i-1])
        
        # The answer is the maximum profit on the last day when not holding stock.
        return not_hold[-1]
    
prices = [1,2,3,0,2]
prices = [1,2,4,2,5,7,2,4,9,0]
prices = [1,2,4,2,5,7,2,4,9,0,9]
prices = [2,6,8,7,8,7,9,4,1,2,4,5,8]

Solution().maxProfit(prices)