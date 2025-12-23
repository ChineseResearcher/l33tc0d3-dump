# dp - medium
from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        n = len(events)
        # offset the startTime for each event by -1 to align with definition in the description
        for i in range(n):
            events[i][0] -= 1

        # sort out 2-D array by the endTime of events and unpack
        startTime, endTime, value = map(list, zip(*sorted(events, key = lambda x: x[1])))

        # construct a dp of size n where dp[i] stores
        # the solution to the subproblem considering only up to events[:i]
        dp = [0] * n

        # initiate dp[0] to be value[0]
        dp[0] = value[0]

        # initiate a dict tracking the value of the most valuable 
        # event that ends before startTime[i], using index i as the key
        prev_max_val = [0] * n
        prev_max_val[0] = value[0]

        fmax = lambda a, b: a if a >= b else b

        def bs(l, r):

            # goal is the rightmost valid index such that
            # endTime[index] <= startTime[initial r]
            time_cutoff = startTime[r]

            rightMost = -1
            while l <= r:

                mid = (l+r) // 2
                if endTime[mid] <= time_cutoff:
                    rightMost = fmax(rightMost, mid)
                    l = mid+1
                else:
                    r = mid-1

            return rightMost

        ans = dp[0]
        for i in range(1, n):
  
            last_non_overlap = bs(0, i)
            if last_non_overlap == -1:
                dp[i] = value[i]
            else:
                dp[i] = prev_max_val[last_non_overlap] + value[i]
            
            ans = fmax(ans, dp[i])
            prev_max_val[i] = fmax(prev_max_val[i-1], value[i])

        return ans
    
events = [[1,3,2],[4,5,2],[2,4,3]]
events = [[1,3,2],[4,5,2],[1,5,5]]
events = [[1,5,3],[1,5,1],[6,6,5]]

Solution().maxTwoEvents(events)