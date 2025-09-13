# dp - medium
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        n = len(intervals)
        intervals.sort()
        
        # storing the maximal overlap an i-th interval is involved in
        dp = [[float('inf'), float('-inf')] for _ in range(n)] 

        for i in range(1,n):
            
            curr, prev = intervals[i], intervals[i-1]
            # determine if there's an overlap
            if curr[0] < prev[1]:

                currOverlap = [max(curr[0], prev[0]), min(curr[1], prev[1])]

                # update the overlap status of i and i-1 intervals
                # update left-end
                dp[i-1][0] = min(dp[i-1][0], currOverlap[0])
                dp[i][0] = min(dp[i][0], currOverlap[0])

                # update right-end
                dp[i-1][1] = max(dp[i-1][1], currOverlap[1])
                dp[i][1] = max(dp[i][1], currOverlap[1])
            
        valid_right = dp[0][1]
        to_remove = []
        for i in range(n-1):
            
            if dp[i+1][0] >= valid_right:
                valid_right = dp[i+1][1]
                
            else:
                if dp[i+1][1] < valid_right:
                    # greedily use the more leftwards right-end
                    valid_right = dp[i+1][1]
                    to_remove.append(intervals[i])
                else:
                    to_remove.append(intervals[i+1])
        
        return len(to_remove)
    
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],
             [58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

Solution().eraseOverlapIntervals(intervals)