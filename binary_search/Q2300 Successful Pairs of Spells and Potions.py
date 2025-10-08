# binary search - medium
from typing import List
import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        n, m = len(spells), len(potions)
        # sort the portions for binary search later
        potions.sort()

        ans = []
        for i in range(n):

            mul = success // spells[i]
            if success % spells[i] != 0:
                mul += 1 # ceiling division

            # find the index s.t. potions[index:] all satisfy
            pos = bisect.bisect_left(potions, mul)
            ans.append(m - pos)

        return ans
    
spells, potions, success = [5,1,3], [1,2,3,4,5], 7
spells, potions, success = [3,1,2], [8,5,8], 16

Solution().successfulPairs(spells, potions, success)