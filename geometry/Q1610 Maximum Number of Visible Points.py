# geometry - hard
import math
from typing import List
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        # key ideas:
        # 1) calculate the angle formed by every point and my east direction,
        # 2) sort the angles, and apply sliding window to find the answer
        X0, Y0 = location[0], location[1]

        def findAngle(x, y):

            # computing the angle would require finding the gradient first
            # however, there's the additional check on which quadrant (x, y) falls
            # in relative to (X0, Y0)
            y_delta = y - Y0
            x_delta = x - X0
            return (math.degrees(math.atan2(y_delta, x_delta)) + 360) % 360

        ovlap = 0
        # process the points and compute angles
        angles = []
        for x, y in points:
            if x == X0 and y == Y0:
                # overlap with viewer
                ovlap += 1
                continue

            angles.append(findAngle(x, y))

        m = len(angles)
        if m == 0:
            return ovlap
            
        angles.sort()

        r = 0
        # potentially set our left pointer to the points in next clockwise quadrant at the start
        for i in range(m-1, -1, -1):
            if 360 - abs(angles[0] - angles[i]) > angle:
                break
        l = (i + 1) % m

        # helper to determine if an angle falls in field of view
        def inView(lb, rb, ang):
            if lb < rb:
                return True if (ang <= lb or ang >= rb) else False
            else:
                return True if (rb <= ang <= lb) else False

        # scan the angles in anti-clockwise manner as if they are
        # the left extreme of the viewer's current viewing angle as he rotates
        maxView = 0
        for r in range(m):
            
            # define right extreme
            lb_angle = angles[r]
            rb_angle = (angles[r] - angle + 360) % 360

            # keep shrinking window if exceeds field of view
            while not inView(lb_angle, rb_angle, angles[l]):
                l = (l + 1) % m

            if r >= l:
                currView = r - l + 1
            else:
                currView = (m - l) + (r + 1)

            if currView > maxView:
                maxView = currView

        return maxView + ovlap

points, angle, location = [[2,1],[2,2],[3,3]], 90, [1,1]
points, angle, location = [[2,1],[2,2],[3,4],[1,1]], 90, [1,1]
points, angle, location = [[1,0],[2,1]], 13, [1,1]
points, angle, location = [[1,1],[2,2],[1,2],[2,1]], 0, [1,1]
# many more WA testcases due to inView checking logic...

Solution().visiblePoints(points, angle, location)