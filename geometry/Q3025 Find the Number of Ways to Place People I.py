# geometry - medium
from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        n = len(points)
        # core ideas:
        # 1) input size is max. 50, so O(n^3) is good enough. We take O(n^2) to explore all
        # coordinate pairs (A, B) s.t. A is at the upper left position relative to B

        # 2) sort the points s.t. it is ASC in x, DESC in y, this makes it convenient and 
        # efficient for us to locate (A, B) pairs
        points.sort(key = lambda x: (x[0], -x[1]))

        def isInSquare(tx, ty):
            return x1 <= tx <= x2 and y2 <= ty <= y1

        ans = 0
        for i in range(1, n):
            for j in range(i):

                x1, y1 = points[j]
                x2, y2 = points[i]
                if x1 > x2 or y1 < y2:
                    continue
                
                isValid = True
                for k in range(n):
                    if k not in [i, j] and isInSquare(points[k][0], points[k][1]):
                        isValid = False
                        break

                if isValid:
                    ans += 1

        return ans
    
points = [[1,1],[2,2],[3,3]]
points = [[6,2],[4,4],[2,6]]
points = [[3,1],[1,3],[1,1]]

Solution().numberOfPairs(points)