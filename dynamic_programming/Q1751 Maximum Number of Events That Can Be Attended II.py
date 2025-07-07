# dp - hard
from typing import List
from functools import cache
import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        n = len(events)
        events.sort()
        sd = [x[0] for x in events]

        @cache
        def recursive_attend(idx, k):

            if k == 0 or idx == n:
                return 0
            
            # op1: skip this event
            curr_res = recursive_attend(idx+1, k)

            # op2: use binary search to find the next admissible event
            j = bisect.bisect_left(sd, events[idx][1]+1)
            if j < n and sd[j] > events[idx][1]:
                curr_res = max(curr_res, events[idx][2] + recursive_attend(j, k-1))
            elif j == n:
                curr_res = max(curr_res, events[idx][2])

            return curr_res

        return recursive_attend(0, k)
    
events, k = [[1,2,4],[3,4,3],[2,3,1]], 2
events, k = [[1,2,4],[3,4,3],[2,3,10]], 2
events, k = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3
events, k = [[21,77,43],[2,74,47],[6,59,22],[47,47,38],[13,74,57],[27,55,27],[8,15,8]], 4

Solution().maxValue(events, k)