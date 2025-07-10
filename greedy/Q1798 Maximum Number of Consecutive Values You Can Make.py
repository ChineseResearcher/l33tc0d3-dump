# greedy - medium
from typing import List
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:

        n = len(coins)
        # important to sort our coins to allow greedy to work
        coins.sort()

        # keep a running sum
        rSum = 0
        for i in range(n):

            # consecutive formation breaks
            if coins[i] > rSum + 1:
                break
            else:
                rSum += coins[i]

        # as stated in the qn, form 0 coins also count as 1
        return rSum - 0 + 1
    
coins = [1,3]
coins = [1,3,4]
coins = [1,1,1,4]
coins = [1,4,10,3,1]
coins = [1,2,6,7,8]

Solution().getMaximumConsecutive(coins)