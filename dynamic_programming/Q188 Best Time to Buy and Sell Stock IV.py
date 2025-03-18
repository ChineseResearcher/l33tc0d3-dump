# dp - hard
# top-down ver.
# initially TLE due to incorrect dfs logic
# we cannot lump buy/sell together as one transaction
# each buy/sell step contributes 1 count and we have skip options for both cases
class Solution:
    def recursive_invest(self, tx_cnt, idx):

        # note that transaction count is incremented whenever
        # we perform a buy/sell, in other words, the parity of
        # tx_cnt is used to determine if we are allowed to buy/sell

        # once we used up transactions allowed OR
        # we have exhausted the prices array, we terminate
        if tx_cnt == 2 * self.k or idx == self.n:
            return 0
        
        if (tx_cnt, idx) in self.dp: 
            return self.dp[(tx_cnt, idx)]
        
        currAns = 0
        # even cnt would mean we have to buy
        if tx_cnt % 2 == 0:
            
            # minus sign in front to indicate a cost incurred
            buy = -self.prices[idx] + self.recursive_invest(tx_cnt+1, idx+1)
            skip = self.recursive_invest(tx_cnt, idx+1)
            currAns = max(currAns, max(buy, skip))

        # odd cnt would mean we need to sell
        else:

            sell = self.prices[idx] + self.recursive_invest(tx_cnt+1, idx+1)
            skip = self.recursive_invest(tx_cnt, idx+1)
            currAns = max(currAns, max(sell, skip))

        self.dp[(tx_cnt, idx)] = currAns
        return currAns

    def maxProfit(self, k, prices):

        self.k, self.prices = k, prices
        self.n = len(self.prices)
        self.dp = dict()

        # at the start, we have made 0 transactions and can choose from prices[0:]
        return self.recursive_invest(0, 0)
    
# bottom-up ver. (from forum) this is very diff. to come up with tbh
class Solution:
    def maxProfit(self, k, prices):

        # notice that the length dimension used for buy/sell dp arrays
        # are the number of transactions allowed + 1, not length of prices
        buy = [-float("inf")] * (k + 1)
        # we look at sell dp arr. for our final answer as we should exited the long pos.
        sell = [-float("inf")] * (k + 1)
        buy[0], sell[0] = 0, 0

        # there's clever usage of states compression -> prices dimensions is gone
        # buy[i]/sell[i] each represents the max. profit attained at the i-th transaction
        # note: we cannot swap the for-loop order
        for p in prices:
            for i in range(1, k + 1):
             
                # the order of updating buy[i] before sell[i] matters as buy[i]
                # needs to reference sell @ i-1 first

                # we can only buy another stock once we 
                # finished the prior transaction with a sell
                buy[i] = max(buy[i], sell[i - 1] - p)

                # once we bought into a position, we need to update
                # the sell[i] with ref. to the curr. i-th buy
                sell[i] = max(sell[i], buy[i] + p)

        # one realisation is that making more net-positive trades
        # definitely results in more greater overall profit compared
        # to making fewew net-positive trades
        return sell[-1]

# bottom-up ver. (gpt), closer to what I wanted to achieve
class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        
        # If k >= n//2, treat as unlimited transactions (like LC122)
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        
        # DP array for k transactions
        dp = [[0] * n for _ in range(k)]

        for t in range(k):
            max_profit_so_far = -prices[0]
            for i in range(1, n):

                # Option 1: No transaction on day i as we inherit dp[t][i-1]
                # Option 2: Transact by selling at prices[i]
                dp[t][i] = max(dp[t][i - 1], prices[i] + max_profit_so_far)
                
                # Update max_profit_so_far for the next day
                # see if we can have a better curr. max profit if we deduct prices[i] from
                # the profit level recorded at the end of the prior transaction
                if t > 0:
                    max_profit_so_far = max(max_profit_so_far, dp[t - 1][i] - prices[i])

                # when t == 0, essentially asking up-to-one transaction problem
                # curr. max profit could be improved with lowering prices
                else:
                    max_profit_so_far = max(max_profit_so_far, -prices[i])
        
        return dp[k-1][n-1]
    
prices = [3,3,5,0,0,3,1,4]
prices = [0,5,0,1,0,10]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [0,3,1,5]
prices = [6,1,3,2,4,7]

Solution().maxProfit(prices)