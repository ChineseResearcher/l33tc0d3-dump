# geometry - medium
from typing import List
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # core ideas:
        # 1) construct the x- and y-axis spanning ranges for the circle and square
        # 2) use linesweep to detect overlapping

        cir_x_range = [xCenter-radius, xCenter+radius]
        # we will leave cir_y_range to be derived from the overlapped
        # part of cir_x_range & sq_x_range

        sq_x_range = [x1, x2]
        sq_y_range = [y1, y2]

        def find_overlapped(i1: List[int], i2: List[int]) -> List[int]:

            # assuming [i1, i2] already sorted
            if i1[1] >= i2[0]:
                return [i2[0], min(i1[1], i2[1])]
            else:
                return []
            
        sl = sorted([cir_x_range, sq_x_range])
        x_ovlp = find_overlapped(sl[0], sl[1])
        if not x_ovlp:
            return False

        def find_y_range(x:int) -> List[float]:
            # note that circle eqn can be rewritten as:
            # (y - y_center)^2 = radius^2 - (x - x_center)^2
            RHS = radius ** 2 - (x - xCenter) ** 2
            sqrt = RHS ** 0.5
            return [-sqrt + yCenter, sqrt + yCenter]

        # deriving the spanning y-axis range for the circle
        # for the relevant x-axis range denoted by x_ovlp

        # one special case is that the x_ovlp already encloses the xCenter
        # of the circle, then surely the cir_y_range would be max. possible
        if x_ovlp[0] <= xCenter <= x_ovlp[1]:
            cir_y_range = [yCenter-radius, yCenter+radius]
        else:
            cir_y_range = [float('inf'), float('-inf')]

            res1 = find_y_range(x_ovlp[0])
            res2 = find_y_range(x_ovlp[1])

            cir_y_range[0] = min(res1[0], res2[0])
            cir_y_range[1] = max(res1[1], res2[1])

        sl = sorted([cir_y_range, sq_y_range])
        y_olvp = find_overlapped(sl[0], sl[1])
        if not y_olvp:
            return False

        return True
    
radius, xCenter, yCenter, x1, y1, x2, y2 = 1, 0, 0, 1, -1, 3, 1
radius, xCenter, yCenter, x1, y1, x2, y2 = 1, 1, 1, 1, -3, 2, -1
radius, xCenter, yCenter, x1, y1, x2, y2 = 1, 0, 0, -1, 0, 0, 1
radius, xCenter, yCenter, x1, y1, x2, y2 = 1415, 807, -784, -733, 623, -533, 1005
radius, xCenter, yCenter, x1, y1, x2, y2 = 2, 8, 6, 5, 1, 10, 4

Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)