# dp - medium
# this question is a similar to Q1235
class Solution:
    def binarySearch(self, l, r, startTime, endTime):

        # goal is the rightmost valid index such that
        # endTime[index] <= startTime[initial r]
        time_cutoff = startTime[r]

        rightMost = -1 # dummy
        while l <= r:

            mid = (l+r) // 2
            # print(mid)
            if endTime[mid] <= time_cutoff:

                rightMost = max(rightMost, mid)
                l = mid+1

            else:
                r = mid-1

        return rightMost

    def maxTwoEvents(self, events):
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
        # event that ends before startTime[i]
        prev_max_val = {0: value[0]}

        for i in range(1, n):
  
            last_non_overlap = self.binarySearch(0, i, startTime, endTime)
            if last_non_overlap == -1:
                dp[i] = value[i]
            else:
                dp[i] = prev_max_val[last_non_overlap] + value[i]
                
            prev_max_val[i] = max(prev_max_val[i-1], value[i])

        return max(dp)
    
events = [[1,3,2],[4,5,2],[2,4,3]]
events = [[1,3,2],[4,5,2],[1,5,5]]
events = [[1,5,3],[1,5,1],[6,6,5]]

Solution().maxTwoEvents(events)