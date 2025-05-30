# geometry - medium
from typing import List
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return -1

        # sort the points first
        points.sort()

        # points.length = 10 at max, implying O(n^4) solution or better
        ans = -1

        # our goal is to locate a valid rectangle as we iterate
        # because of the way our points are sorted, we are always searching in the order:
        # bottom left (bl) -> upper left(ul) -> bottom right(br) -> upper right[ur]
        for bl in range(n-3):

            x, y = points[bl][0], points[bl][1]
            for ul in range(bl+1, n-2):

                y_ = points[ul][1]
                if points[ul][0] == x:

                    for br in range(ul+1, n-1):
                        
                        if points[br][0] > x and y < points[br][1] <= y_:
                            break
                        
                        if points[br][1] == y:
                            x_ = points[br][0]
                            for ur in range(br+1, n):

                                if points[ur][1] != y_:
                                    break

                                if points[ur][0] == x_ and points[ur][1] == y_:
                                    ans = max(ans, (x_ - x) * (y_ - y))
                                    break

                            break

                    break

        return ans
    
points = [[1,1],[1,3],[3,1],[3,3]]
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
points = [[100,80],[67,79],[100,79],[67,80],[80,47]]
points = [[87,89],[22,77],[87,77],[87,52],[22,93],[87,93]]

Solution().maxRectangleArea(points)