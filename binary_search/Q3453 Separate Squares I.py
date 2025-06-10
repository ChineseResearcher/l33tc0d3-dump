# binary search - medium
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # binary search is helpful for this task as there's 
        # monotonicity in determining the min. possible y-axis

        # the search bounds [l,r] would be init. to the lowest
        # and highest possible y-axis provided in the squares arr.
        l, r = float('inf'), 0
        for _, y, len in squares:
            l = min(l, y)
            r = max(r, y + len)

        # write a linear time checker to determine if curr.
        # y-axis indeed splits area into two equal halves
        def getArea(yh, squares):

            area_top, area_bot = 0, 0
            for _, y, len in squares:
                
                area_top += min(max(y + len - yh, 0), len) * len
                area_bot += min(max(yh - y, 0), len) * len

            return area_top, area_bot

        epsilon = 1e-5
        # the key realisation is that we converge on l, r, NOT on above/below areas
        while r - l > epsilon:

            yh = (l + r) / 2
            at, ab = getArea(yh, squares)

            if at > ab:
                l = yh
            elif at <= ab:
                r = yh

        return (l + r) / 2
    
squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]
squares = [[106,193,36],[139,195,14]]
squares = [[11,158,46],[85,171,47],[31,199,46]]
squares = [[172,197,54],[67,161,87]]
squares = [[13,21,6],[15,18,1],[10,15,3]]

Solution().separateSquares(squares)