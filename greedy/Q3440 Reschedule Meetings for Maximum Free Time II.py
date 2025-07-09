# greedy - medium
from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:

        n = len(startTime)
        # construct an auxiliary arr. to store the free gaps
        free, free_cnt = [], 0

        # consider the first possible gap w.r.t time 0
        free.append(startTime[0] - 0)
        free_cnt += 1 if free[-1] > 0 else 0

        for i in range(1, n):
            free.append(startTime[i] - endTime[i-1])
            free_cnt += 1 if free[-1] > 0 else 0

        # consider the last possible gap w.r.t. to eventTime
        free.append(eventTime - endTime[-1])
        free_cnt += 1 if free[-1] > 0 else 0

        # no improvement in max. continuous free time possible
        # if there are one or fewer "free" gaps to begin with
        if free_cnt <= 1:
            return sum(free)

        m = n + 1

        # we need to build prefix & postfix arrs. to record the
        # max. gap possible before and after index i
        pre_max, post_max = [0] * m, [0] * m

        for k in range(1, m):
            pre_max[k] = max(free[k-1], pre_max[k-1])

        for k in range(m-2, -1, -1):
            post_max[k] = max(free[k+1], post_max[k+1])

        ans = 0
        # explore reschedule options
        # note: we are guaranteed that free_cnt >= 3
        for j in range(1, m):

            # ref. the length of curr. meeting
            ml = endTime[j-1] - startTime[j-1]

            # validate if there are any nonzero gaps 
            # prior to j-1 OR post to j that would fit this meeting
            if pre_max[j-1] >= ml or post_max[j] >= ml:
                ans = max(ans, free[j-1] + free[j] + ml)

            else:
                ans = max(ans, free[j-1] + free[j])

        return ans
    
eventTime, startTime, endTime = 5, [1,3], [2,5]
eventTime, startTime, endTime = 10, [0,7,9], [1,8,10]
eventTime, startTime, endTime = 10, [0,3,7,9], [1,4,8,10]
eventTime, startTime, endTime = 5, [0,1,2,3,4], [1,2,3,4,5]
eventTime, startTime, endTime = 41, [17,24], [19,25]
eventTime, startTime, endTime = 52, [28,38], [38,41]

Solution().maxFreeTime(eventTime, startTime, endTime)