# geometry - easy
from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        n = len(points)
        # find triangle area using determinants
        # where for three vertices (a, b), (c, d), (e, f)
        # area = 0.5 * |a * (d-f) + c * (f-b) + e * (b-d)|

        ans = 0
        for i in range(n-2):
            a, b = points[i]

            for j in range(i+1, n-1):
                c, d = points[j]

                for k in range(j+1, n):
                    e, f = points[k]
                    
                    area = abs(a * (d-f) + c * (f-b) + e * (b-d))
                    if area > ans:
                        ans = area

        return ans / 2    
    
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
points = [[1,0],[0,0],[0,1]]

Solution().largestTriangleArea(points)