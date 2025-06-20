# sliding window - medium
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        prevEnd = 0
        # first collect all free gaps into an arr.
        free = []
        for i in range(n):
            
            # since we are given non-overlapping events, the free gap
            # is at least 0, and recording 0 is important as it disallows
            # merging non-adjacent gaps
            free.append(startTime[i] - prevEnd) 
            prevEnd = endTime[i]

        if eventTime > endTime[-1]:
            free.append(eventTime - endTime[-1])

        if not free:
            return 0

        # for k moves allowed, it means we could merge k+1
        # consecutive free gaps at most, so we explore a fixed sliding window
        wl = min(k + 1, len(free))
        ans = sum(free[:wl])

        curr = ans
        for j in range(wl, len(free)):

            curr += free[j]
            curr -= free[j-wl]
            ans = max(ans, curr)

        return ans
    
eventTime, k, startTime, endTime = 5, 1, [1,3], [2,5]
eventTime, k, startTime, endTime = 10, 1, [0,2,9], [1,4,10]
eventTime, k, startTime, endTime = 5, 2, [0,1,2,3,4], [1,2,3,4,5]
eventTime, k, startTime, endTime = 34, 2, [0,17], [14,19]
eventTime, k, startTime, endTime = 21, 1, [7,10,16], [10,14,18]

Solution().maxFreeTime(eventTime, k, startTime, endTime)