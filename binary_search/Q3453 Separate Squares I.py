# binary search - medium
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # binary search is helpful for this task as there's 
        # monotonicity in determining the min. possible y-axis

        # the search bounds [l,r] would be init. to the lowest
        # and highest possible y-axis provided in the squares arr.
        l, r, area_all = float('inf'), 0, 0
        for _, y, len in squares:
            l = fmin(l, y)
            r = fmax(r, y + len)
            area_all += pow(len, 2)

        # write a linear time checker to determine if curr.
        # y-axis indeed splits area into two equal halves
        def getArea(yh, squares):

            area_top = 0
            for _, y, len in squares:
                area_top += fmin(fmax(y + len - yh, 0), len) * len

            return area_top, area_all - area_top

        epsilon = 1e-5
        # the key realisation is that we converge on l, r, NOT on above/below areas
        while r - l > epsilon:

            yh = (l + r) / 2
            at, ab = getArea(yh, squares)

            if at > ab:
                l = yh
            elif at <= ab:
                r = yh

        return (l + r) / 2

# line sweep - much faster
from collections import defaultdict
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:   

        # key ideas:
        # 1) we can make use of sweep line algorithm from low to high in the y-dim
        # 2) maintain a diff dict and sort non-zero diff points in ascending order
        diff = defaultdict(int)

        total_area, y_min = 0, float('inf')
        for _, y, l in squares:
            y_min = min(y_min, y)
            diff[y] += l
            diff[y+l] -= l

            total_area += pow(l, 2)

        half_area = total_area / 2
        # curr indicates the area to add/subtract at each diff point
        curr, acc_area, prev_k = 0, 0, y_min

        ans = -1
        for k in sorted(diff.keys()):
            
            if acc_area + curr * (k - prev_k) >= half_area:
                ans = prev_k + (half_area - acc_area) / curr 
                break
            
            acc_area += curr * (k - prev_k)
            curr += diff[k]
            prev_k = k

        return ans
    
squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]
squares = [[106,193,36],[139,195,14]]
squares = [[11,158,46],[85,171,47],[31,199,46]]
squares = [[172,197,54],[67,161,87]]
squares = [[13,21,6],[15,18,1],[10,15,3]]

Solution().separateSquares(squares)