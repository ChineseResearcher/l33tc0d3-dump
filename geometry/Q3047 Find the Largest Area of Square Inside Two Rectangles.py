# geometry - medium
from typing import List
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:

        n = len(bottomLeft)
        # helper to determine intersecting line width of
        # two lines denoted by [a...b] and [c...d]
        def get_ovlap(a:int, b:int, c:int, d:int) -> int:

            l = [(a,b), (c,d)]
            l.sort()

            if l[1][0] >= l[0][1]:
                return 0
            return min(l[0][1], l[1][1]) - l[1][0]

        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        max_ovlap = 0
        for i in range(n-1):
            for j in range(i+1, n):
                x_ovlap = get_ovlap(bottomLeft[i][0], topRight[i][0], 
                                    bottomLeft[j][0], topRight[j][0])
                if x_ovlap == 0:
                    continue
                
                y_ovlap = get_ovlap(bottomLeft[i][1], topRight[i][1], 
                                    bottomLeft[j][1], topRight[j][1])
                if y_ovlap == 0:
                    continue

                max_ovlap = fmax(max_ovlap, fmin(x_ovlap, y_ovlap))

        return pow(max_ovlap, 2)
    
bottomLeft, topRight = [[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]
bottomLeft, topRight = [[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]
bottomLeft, topRight = [[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]]

Solution().largestSquareArea(bottomLeft, topRight)