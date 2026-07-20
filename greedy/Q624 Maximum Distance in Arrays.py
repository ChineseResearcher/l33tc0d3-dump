# greedy - medium
from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        n = len(arrays)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) maintain prefix min / max number seen based on arrays[i][0]
        # 2) for every new arrays[i][1], try to build a bigger diff using prefix min

        ans, pf_min, pf_max = 0, float('inf'), float('-inf')
        for i in range(n):
            curr_min, curr_max = arrays[i][0], arrays[i][-1]
            ans = fmax(ans, curr_max - pf_min)
            ans = fmax(ans, pf_max - curr_min)
            
            # update min / max
            pf_min = fmin(pf_min, curr_min)
            pf_max = fmax(pf_max, curr_max)

        return ans

arrays = [[1],[1]]
arrays = [[1,2,3],[4,5],[1,2,3]]

Solution().maxDistance(arrays)