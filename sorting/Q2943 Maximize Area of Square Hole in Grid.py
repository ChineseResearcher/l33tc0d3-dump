# sorting - medium
from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        # key ideas:
        # 1) the biggest squared hole arises from the longest common length
        # that we could free-up from both vertical and horizontal directions

        # 2) finding that longest common length requires sorting and linear
        # passes to hBars and vBars to find the longest free section

        fmax = lambda a, b: a if a > b else b

        hBars.sort()
        # set prev. un-removable to the bar before hBars[0]
        prev, h_best = hBars[0]-1, 0
        for i in range(len(hBars)-1):
            # non-contiguous detected
            if hBars[i+1] > hBars[i] + 1:
                h_best = fmax(h_best, hBars[i] + 1 - prev)
                prev = hBars[i+1] - 1

        # obtain max. w.r.t to last bar too
        h_best = fmax(h_best, hBars[-1]+1-prev)

        # do the same thing vertically
        vBars.sort()
        prev, v_best = vBars[0]-1, 0
        for i in range(len(vBars)-1):
            if vBars[i+1] > vBars[i] + 1:
                v_best = fmax(v_best, vBars[i] + 1 - prev)
                prev = vBars[i+1] - 1

        v_best = fmax(v_best, vBars[-1]+1-prev)

        # max. square's side length is then constrained by min. of two best lengths
        return pow(min(h_best, v_best), 2)
    
n, m, hBars, vBars = 2, 1, [2,3], [2]
n, m, hBars, vBars = 1, 1, [2], [2]
n, m, hBars, vBars = 2, 3, [2,3], [2,4]
n, m, hBars, vBars = 2, 4, [3,2], [4,2]
n, m, hBars, vBars = 14, 4, [13], [3,4,5,2]

Solution().maximizeSquareHoleArea(n, m, hBars, vBars)