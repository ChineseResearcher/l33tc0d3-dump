# geometry - medium
from typing import List
from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) find out the 1-cells in both grids and record them in separate lists
        # 2) group the cell counts by linear transformations in terms of delta x & y
        # 3) track the group with largest count
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        cnt = defaultdict(int)
        
        ans = 0
        for ax, ay in A:
            for bx, by in B:
                dx = bx - ax
                dy = by - ay
                cnt[(dx, dy)] += 1
                ans = fmax(ans, cnt[(dx, dy)])
                
        return ans

img1, img2 = [[0]], [[0]]
img1, img2 = [[1]], [[1]]
img1, img2 = [[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]

Solution().largestOverlap(img1, img2)