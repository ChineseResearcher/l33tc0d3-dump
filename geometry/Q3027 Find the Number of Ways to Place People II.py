# geometry - hard
from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        n = len(points)
        # core ideas:
        # 1) sort the points s.t. we have x-axis ASC and y-axis DESC
        # 2) for each points[i], explore all points[j] s.t.
        # (a) j < i and points[j] is a valid top-left coordinate relative to points[i]
        # 3) optimisation to achieve O(n^2)
        points.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        for i in range(1, n):
            
            # points[i] act as the bottom right coordinate
            x_br, y_br = points[i]

            # minimise y of the top left coordinate
            y_max = float('inf')
            for j in range(i-1, -1, -1):

                # notice that x-axis position of top (upper) left does not matter
                # as we've already sorted x-axis in ASC order so x_ul <= x_br for sure
                _, y_ul = points[j]

                # enforce top-left relative position
                if y_ul < y_br:
                    continue
                
                if y_ul < y_max:
                    ans += 1
                    y_max = min(y_max, y_ul)

        return ans
    
points = [[1,1],[2,2],[3,3]]
points = [[6,2],[4,4],[2,6]]
points = [[3,1],[1,3],[1,1]]

Solution().numberOfPairs(points)