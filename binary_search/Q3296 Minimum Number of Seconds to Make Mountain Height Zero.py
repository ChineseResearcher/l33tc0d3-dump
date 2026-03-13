# binary search - medium
import math
from typing import List
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        fmin = lambda a, b: a if a < b else b
        # sort workers by efficiency
        workerTimes.sort()

        # a helper to find the max. height reducible 
        # given workerTimes wt and a time limit of target
        def max_reduce(target:int, wt: int) -> int:
            return math.floor((pow(1 + 8 * target / wt, 0.5) - 1) / 2)

        # check if it is possible to reduce entire mountainHeight
        # given a time limit of target
        def possible(target:int) -> bool:
            h = mountainHeight
            for wt in workerTimes:
                h -= max_reduce(target, wt)
                if h <= 0:
                    break

            return h <= 0

        # we need a bit of simulation to determine the right bound
        # for binary search on the min. time 
        mul, r = 0, 0
        while mul * len(workerTimes) < mountainHeight:
            mul += 1
            # min. time determined by the worker w/ worst efficiency
            r = workerTimes[-1] * (mul * (mul + 1) // 2)

        l, ans = 1, float('inf')
        while l <= r:

            target = (l + r) // 2
            if possible(target):
                ans = fmin(ans, target)
                r = target - 1
            else:
                l = target + 1

        return ans
    
mountainHeight, workerTimes = 5, [1]
mountainHeight, workerTimes = 4, [2,1,1]
mountainHeight, workerTimes = 10, [3,2,2,4]

Solution().minNumberOfSeconds(mountainHeight, workerTimes)