# simulation - medium
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        ans, empty = numBottles, numBottles
        while empty >= numExchange:

            # we could only exchange for 1 full bottle once
            empty -= numExchange
            empty += 1 # drink immediately
            ans += 1

            # increment exchange requirement
            numExchange += 1

        return ans
    
numBottles, numExchange = 13, 6
numBottles, numExchange = 10, 3

Solution().maxBottlesDrunk(numBottles, numExchange)