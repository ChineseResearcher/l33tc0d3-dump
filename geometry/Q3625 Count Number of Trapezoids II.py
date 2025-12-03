# geometry - hard
import math
from collections import defaultdict
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        n = len(points)
        # key ideas:
        # 1) store unique gradients arising from every pair of points,
        # note that there's maximally O(n^2) pairs

        # 2) for each unique gradient, store the count of the lines
        # w/ unique y- or x-axis intercepts with a dict

        cnt = dict() # <gradient: <intercept: cnt>>
        midpoint = dict() # <mid-pt coord: <gradient: cnt>>

        def gcd_reduce(a, b):
            # given a fraction in the form of a / b
            # reduce them to the simplest form
            common = math.gcd(a, b)
            return (a // common, b // common)

        def sign_help(a, b):
            # take care of sign, -ve always load to first term
            if a < 0 and b < 0:
                return (-a, -b)
            elif a < 0:
                return (a, b)
            elif b < 0:
                return (-a, -b)
            else:
                return (a, b)
            
        def get_grad(x0, y0, x1, y1):

            # vertical line
            if x0 == x1:
                return (float('inf'), -1)
            
            # horizontal line
            if y0 == y1:
                return (0, -1)
            
            x_delta, y_delta = x0 - x1, y0 - y1
            # return gradient as a fraction in simplest form
            a, b = gcd_reduce(y_delta, x_delta)
            return sign_help(a, b)
            
        def get_intercept(a, b, x, y):
            # suppose y = (a/b) * x + c where c is the intercept
            # the intercept can be found as (by - ax) / b
            top = b * y - a * x
            bottom = b

            if top == 0:
                return (0, -1)
            
            # again reduce by gcd
            top, bottom = gcd_reduce(top, bottom)
            return sign_help(top, bottom)
            
        # process the points
        for i in range(n-1):
            for j in range(i+1, n):

                x0, y0 = points[i][0], points[i][1]
                x1, y1 = points[j][0], points[j][1]

                grad = get_grad(x0, y0, x1, y1)
                if grad[0] == float('inf'):
                    intercept = x0
                elif grad[0] == 0:
                    intercept = y0
                else:
                    intercept = get_intercept(grad[0], grad[1], x0, y0)

                if grad not in cnt:
                    cnt[grad] = defaultdict(int)

                cnt[grad][intercept] += 1

                # increment mid-point dict
                x_mid = (x0 + x1) / 2
                y_mid = (y0 + y1) / 2

                if (x_mid, y_mid) not in midpoint:
                    midpoint[(x_mid, y_mid)] = defaultdict(int)

                midpoint[(x_mid, y_mid)][grad] += 1

        ans = 0
        # for each unique gradient, we calculate the unique trapezoids formed
        for _, inner_dict in cnt.items():

            pairCnt = sum(inner_dict.values())
            for _, c in inner_dict.items():

                pairCnt -= c
                ans += c * pairCnt

        # we need to discount the number of parallelograms from the answer
        for _, inner_dict in midpoint.items():

            pairCnt = sum(inner_dict.values())
            for _, c in inner_dict.items():

                pairCnt -= c
                ans -= c * pairCnt

        return ans

points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
points = [[0,0],[1,0],[0,1],[2,1]]
points = [[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]]

Solution().countTrapezoids(points)