# heap - medium
from typing import List
import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        # first sort intervals
        intervals.sort()

        # construct a minheap to store the endTime of a group
        minheap = [0]

        for l, r in intervals:

            # even the group w/ the earliest endTime could not
            # avoid an intersection with the curr. interval
            if l <= minheap[0]:
                heapq.heappush(minheap, r)

            else:
                heapq.heappop(minheap)
                heapq.heappush(minheap, r)

        # the number of items in minheap 
        # indicates the count of active groups
        return len(minheap)
    
intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
intervals = [[1,3],[5,6],[8,10],[11,13]]

Solution().minGroups(intervals)