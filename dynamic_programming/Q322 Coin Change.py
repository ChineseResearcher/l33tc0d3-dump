# dp - medium
class Solution:
    def coinChange(self, coins, amount):
        
        coinSet = set(coins)
        dp = [float('inf')] * (amount+1)

        # you can always make up 0 dollar without using any coins
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coinSet:
                if i - coin >= 0: 
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[amount] if dp[amount] < float('inf') else -1
    
coins, amount = [1,2,5], 11
coins, amount = [2], 3
coins, amount = [1], 0
coins, amount = [156,265,40,280], 9109

Solution().coinChange(coins, amount)