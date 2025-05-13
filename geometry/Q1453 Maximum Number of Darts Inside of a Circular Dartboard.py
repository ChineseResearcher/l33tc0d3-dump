# geometry - hard
from typing import List
class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        # main idea:
        # 1) use O(n^2) to explore all pairs of coordinates, and find out their intersection(s)
        # 2) use additional O(n) time to check how many points 
        # fall within the circle(s) centered at the found intersection(s)
        def cntWithin(cx, cy, epsilon=1e-5):

            cnt = 0
            for x, y in darts:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2 + epsilon:
                    cnt += 1

            return cnt

        def find_two_intersections(a, b, c, d, r):
            # given two circles in the general form of:
            # (x-a)^2 + (y-b)^2 = r^2
            # (x-c)^2 + (y-d)^2 = r^2
            # find the two intersections point of these two circles
            # note: implies that distance between (a,b) and (c,d) < 2 * r

            # first get the mid-point
            mx, my = (a + c) / 2, (b + d) / 2 

            # special case 1: 
            # if gradient of line passing through both points has 0 gradient
            # then the tangent passing through two intersections has inf. gradient
            if d - b == 0:

                # tangent at mx
                res_sqrt = (r ** 2 - (mx - a) ** 2) ** 0.5
                return (mx, res_sqrt + b), (mx, -res_sqrt + b)

            # special case 2:
            # opposite of (1)
            elif c - a == 0:

                # targent at my
                res_sqrt = (r ** 2 - (my - b) ** 2) ** 0.5
                return (res_sqrt + a, my), (-res_sqrt + a, my)

            # otherwise we have a normal tangent gradient
            else:

                # since y can be expressed by x s.t. y = kx + g
                # we can transform (x-a)^2 + (y-b)^2 = r^2 into:
                # (x-a)^2 + (kx + g - b)^2 = r^2
                # with some algebra, the coefficients of x^2, x and constant can be found

                # first find the gradient of tangent
                k = -(c - a) / (d - b)
                g = (c ** 2 - a ** 2) / (2 * (d - b)) + (d + b) / 2

                # coeff of x^2
                A = 1 + k ** 2

                # coeff of x
                B = 2 * ((g - b) * k - a)

                # const
                C = a ** 2 + (g - b) ** 2 - r ** 2

                res_sqrt = (B ** 2 - 4 * A * C) ** 0.5
                x1 = (-B + res_sqrt) / (2 * A)
                y1 = k * x1 + g

                x2 = (-B - res_sqrt) / (2 * A)
                y2 = k * x2 + g

                return (x1, y1), (x2, y2)

        # answer is at least one because r is non-negative
        ans = 1
        for i in range(n-1):
            for j in range(i+1, n):

                a, b = darts[i]
                c, d = darts[j]

                # find distance between (a,b) and (c,d) squared
                d_sq = (a - c) ** 2 + (b - d) ** 2

                # only one intersection (circle) found
                if d_sq == 4 * r ** 2:
                    ans = max(ans, cntWithin((a + c) / 2, (b + d) / 2))

                # two intersections guaranteed
                elif d_sq < 4 * r ** 2:
                    center1, center2 = find_two_intersections(a, b, c, d, r)

                    cx, cy = center1
                    ans = max(ans, cntWithin(cx, cy))

                    cx, cy = center2
                    ans = max(ans, cntWithin(cx, cy))

        return ans
    
darts, r = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5
darts, r = [[-2,0],[2,0],[0,2],[0,-2]], 2
darts, r = [[-2,0],[2,0],[0,2],[0,-2]], 1

Solution().numPoints(darts, r)