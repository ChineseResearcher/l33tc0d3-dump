# array - medium
from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        # key ideas:
        # 1) performing counting sort by building a freq. arr. for each
        # distinct integer in range [0, max(costs)]
        # 2) collect the sorted arr. by iterating thru the freq. arr.
        # 3) at the same time determine the number of ice cream bars purchased

        maxC = max(costs)
        freq = [0] * (maxC + 1)
        for c in costs:
            freq[c] += 1

        ans = 0
        for c, f in enumerate(freq):
            taken = 0
            while taken < f:
                # ran out of coins
                if coins - c < 0:
                    return ans
                coins -= c
                ans += 1
                taken += 1

        # case where coins are enough to purchase all
        return ans

costs, coins = [1,3,2,4,1], 7
costs, coins = [10,6,8,7,7,8], 5
costs, coins = [1,6,3,1,2,5], 20

Solution().maxIceCream(costs, coins)