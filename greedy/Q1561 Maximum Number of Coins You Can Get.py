# greedy - medium
from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles)
        # goal is to pick all the second largest pile 
        # of the three piles picked at every step
        # greedy thinking: since Alice has to pick a larger pile than me
        # then picking will be alternating between Alice and me from high to low
        piles.sort(reverse=True)

        # length considered by Alice and me
        m = (n // 3) * 2

        ans = 0
        for i in range(1, m, 2):
            ans += piles[i]

        return ans

piles = [2,4,5]
piles = [2,4,1,2,7,8]
piles = [9,8,7,6,5,1,2,3,4]

Solution().maxCoins(piles)