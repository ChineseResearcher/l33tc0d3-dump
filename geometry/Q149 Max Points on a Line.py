from collections import defaultdict
import math

class Solution:
    def get_simp_frac(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd

    def cal_grad_disp(self, x1, y1, x2, y2):
        # given two pairs of coords, find the params of linear
        # equation of the line passing through the two points

        # vert. straight line
        if x1 == x2:
            grad, disp = float('inf'), x1
        # horizontal straight line
        elif y1 == y2:
            grad, disp = 0, y1
        else:
            grad_num, grad_denom = y2 - y1, x2 - x1
            grad_num, grad_denom = self.get_simp_frac(grad_num, grad_denom)

            grad = grad_num / grad_denom

            disp_num, disp_denom = y2 * grad_denom - grad_num * x2, grad_denom
            disp_num, disp_denom = self.get_simp_frac(disp_num, disp_denom)

            disp = disp_num / disp_denom

        # return computed gradient & displacement
        return grad, disp

    def solve_quadratic(self, a, b, c):
        # guaranteed integer solution
        return int( (-b + (b**2 - 4 * a * c) ** 0.5) / 2*a )

    def maxPoints(self, points):
        
        n = len(points)
        # there can be 300 points at max.
        # which means there can be 300 * 299 / 2 = 44850 possible pairs

        # store the lines found in <gradient, displacement> unique keys
        lines = defaultdict(int)

        for i in range(n-1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):

                x2, y2 = points[j][0], points[j][1]
                grad, disp = self.cal_grad_disp(x1, y1, x2, y2)
                lines[(grad, disp)] += 1

        # one point is considered a line
        ans = 1
        for v in lines.values():

            # note that every count recorded is a result of nC2 where
            # n is the actual number of points on the line
            ans = max(ans, self.solve_quadratic(1, -1, -2*v))

        return ans
    
points = [[1,1],[2,2],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points = [[-6,-1],[3,1],[12,3]]

Solution().maxPoints(points)