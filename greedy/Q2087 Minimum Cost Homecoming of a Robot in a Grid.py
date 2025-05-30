# greedy - medium
from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        x, y = startPos
        hx, hy = homePos

        if x == hx and y == hy:
            return 0

        dx, dy = hx - x, hy - y 

        ans = 0
        # compute vertical move cost
        ans += sum(rowCosts[x+1: x+dx+1]) if dx >= 0 else sum(rowCosts[x+dx: x])

        # compute horizontal move cost
        ans += sum(colCosts[y+1: y+dy+1]) if dy >= 0 else sum(colCosts[y+dy: y])

        return ans
    
startPos, homePos, rowCosts, colCosts = [1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]
startPos, homePos, rowCosts, colCosts = [0, 0], [0, 0], [5], [26]

Solution().minCost(startPos, homePos, rowCosts, colCosts)