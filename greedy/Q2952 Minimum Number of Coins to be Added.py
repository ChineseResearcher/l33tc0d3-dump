# greedy - medium
from typing import List
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        # idea is to keep track the the currSum (where the added coins would be included too)
        # and always find the next smallest un-buildable sum, and add it as a coin

        # suppose we are given coins [1,2],
        # if we leave the target aside and focus on what's the next smallest unbuilable sum
        # by induction we figure out is the running sum + 1 (i.e. (1+2)+1 = 4)
        # and if we add coin 4, we can be sure that we can build numbers all the way up to
        # 1 + 2 + 4 = 7, and that the next unbuildable sum is 7 + 1 = 8 (by induction)

        # sort the coins as we want to greedily find the next smallest unbuildsable coin sum
        coins.sort()

        currSum = 0
        n = len(coins)
        neededCoins = []

        while currSum + 1 < coins[0]:
            
            if currSum >= target:
                return len(neededCoins)

            neededCoins.append(currSum+1)
            currSum += (currSum+1)

        for i in range(n-1):
            currSum += coins[i]
            if currSum >= target:
                break

            # visualse coins = [1,12,15], target = 43 to see why
            # we expect 4 more coins to be added
            while coins[i+1] > currSum + 1:
                # define next smallest unbuildable sum
                neededCoins.append(currSum+1)
                currSum += (currSum+1)

        # last coin was not added to sum as we only loop until i < n-1
        currSum += coins[-1]  

        # extending the coins beyond its original
        while currSum < target:

            neededCoins.append(currSum+1)
            currSum += (currSum+1)

        return len(neededCoins)
    
coins, target = [1,4,10], 19
coins, target = [1,4,10,5,7,19], 19
coins, target = [1,1,1], 20
coins, target = [100000], 100000
coins, target = [2,13,7,1,11], 35
coins, target = [15,1,12], 43

Solution().minimumAddedCoins(coins, target)