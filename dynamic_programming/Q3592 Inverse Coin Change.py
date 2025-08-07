# dp - medium
from typing import List
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:

        n = len(numWays)
        # core ideas:
        # 1) find the smallest denomination first. How?
        # the smallest denomination will be the smallest i s.t. numWays[i] = 1
        # this is because there's only 1 way to form amount i using denomination i

        # 2) our denomination set start w/ the found denomination in (1)
        # and we gradually expand our set

        # 3) how is a new denomination identified?
        # it's important to see that for every numWays[i],
        # we are solving a coin change II problem that sums to amount = numWays[i]
        # w/ some set of found denominations, and if dp[i] happens to be
        # exactly 1 smaller than numWays[i], we know that i itself has to
        # be appended as a new denomination

        ans = []
        # locate the first denomination
        for i, numWay in enumerate(numWays):
            if numWay == 1:
                ans.append(i+1)
                break

        for i, numWay in enumerate(numWays):
            amount = i + 1
            dp = [0] * (n + 1)
            dp[0] = 1 # always possible to form amount 0 using no coins

            for coin in ans:
                for coinSum in range(coin, amount + 1):
                    dp[coinSum] += dp[coinSum - coin]

            if dp[amount] > numWay or dp[amount] < numWay - 1:
                return []

            if dp[amount] == numWay - 1:
                ans.append(amount)

        return ans
    
numWays = [0,1,0,2,0,3,0,4,0,5]
numWays = [1,2,2,3,4]
numWays = [1,2,3,4,15]

Solution().findCoins(numWays)