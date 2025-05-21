# heap - hard
from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # transform the queries such that we are processing from smallest
        # to largest, while keeping track of the indices
        q = sorted([(num, idx) for idx, num in enumerate(queries)])

        # build a minheap indexed by interval length
        minheap = []

        intervals.sort()
        # pointer to access intervals
        iidx = 0

        # prepare the ans arr.
        ans = [0] * len(queries)

        for num, idx in q:
            
            while iidx < len(intervals) and intervals[iidx][0] <= num:
                if num  <= intervals[iidx][1]:
                    heapq.heappush(minheap, [intervals[iidx][1] - intervals[iidx][0] + 1, 
                                            intervals[iidx][0]])
                iidx += 1
                
            if not minheap or (minheap and num < minheap[0][1]):
                ans[idx] = -1
                continue
                
            # lazy-delete mismatched intervals
            while minheap and num >= minheap[0][1] + minheap[0][0]:
                heapq.heappop(minheap)
                
            if minheap:
                ans[idx] = minheap[0][0]
            else:
                ans[idx] = -1
                
        return ans
    
intervals, queries = [[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]
intervals, queries = [[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]
intervals, queries = [[4,5],[5,8],[1,9],[8,10],[1,6]], [7,9,3,9,3]
intervals, queries = [[9,9],[6,7],[5,6],[2,5],[3,3]], [6,1,1,1,9]

Solution().minInterval(intervals, queries)