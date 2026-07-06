# sorting - medium
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) perform sorting s.t. we have left bound ASC, and right bound DESC
        # 2) keep track of prefix max. right bound
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans, pf_rb = 0, -1
        for l, r in intervals:
            if pf_rb >= r:
                continue
            ans += 1
            pf_rb = fmax(pf_rb, r)

        return ans

intervals = [[1,4],[2,3]]
intervals = [[1,4],[3,6],[2,8]]
intervals = [[1,2],[1,4],[3,4]]

Solution().removeCoveredIntervals(intervals)