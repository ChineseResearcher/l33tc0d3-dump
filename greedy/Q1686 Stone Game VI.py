# greedy - medium
from typing import List
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        n = len(aliceValues)
        # key ideas:
        # 1) if a player picks a stone, he not only earns the value defined for him
        # but also prevents the other player from gaining value on this stone, the combined
        # net gain can be intuitively captured by the sum of 2 values for the same stone
        # 2) since both players play optimally, they will both try to maximise the combined
        # value 

        total = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        total.sort(key=lambda k:k[0], reverse=True)

        alice, bob = 0, 0
        for i in range(n):
            if i % 2 == 0:
                alice += aliceValues[total[i][1]]
            else:
                bob += bobValues[total[i][1]]

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0

aliceValues, bobValues = [1,3], [2,1]
aliceValues, bobValues = [1,2], [3,1]
aliceValues, bobValues = [2,4,3], [1,6,7]

Solution().stoneGameVI(aliceValues, bobValues)