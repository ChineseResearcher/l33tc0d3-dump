# heap - medium
from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        n = len(events)
        events.sort()

        # sorting by start date + minheap of end date
        sd, ed = events[0][0], max([x[1] for x in events])

        idx, minheap, ans = 0, [], 0
        for d in range(sd, ed+1):

            # enqueue all events that have a start date >= d
            while idx < n and d >= events[idx][0]:
                heapq.heappush(minheap, events[idx][1])
                idx += 1

            # discard all end dates <= d
            while minheap and minheap[0] < d:
                heapq.heappop(minheap)

            if minheap and d <= minheap[0]:
                heapq.heappop(minheap)
                ans += 1

        return ans
    
events = [[1,2],[2,3],[3,4]]
events = [[1,2],[2,3],[3,4],[1,2]]
events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
events = [[1,5],[1,5],[1,5],[2,3],[2,3]]

Solution().maxEvents(events)