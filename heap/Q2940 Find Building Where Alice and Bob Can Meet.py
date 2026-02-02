# heap - hard
import heapq
from typing import List
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        n = len(heights)
        # handle the queries
        ans = [-1] * len(queries)

        # build an auxiliary array storing deferred queries
        # in which we have deferred[b_j] storing (heights[a1], idx1), (heights[a2], idx2)... (heights[a_i], idx_i)
        # s.t. it is guaranteed for every index pair (a_i, b_j) where 0 <= i,j < n
        # 1) a < b 2) heights[a] >= heights[b] (otherwise it would have been captured in case 2)
        deferred = [ [] for _ in range(n) ]
        
        for idx, q in enumerate(queries):
            
            # assign near/far according to relative position in a query
            near, far = min(q), max(q)
            
            # direct assignment case 1: both are already positioned at the same building
            if near == far:
                ans[idx] = far
                continue
                
            # direct assignment case 2: the far index is the answer
            if heights[far] > heights[near]:
                ans[idx] = far
                continue
                
            # if the above fails, means we need to find a common next greater height
            # the nearest of such would be appended, else append -1
            
            # this is done by first storing such queries to deferred array first
            deferred[far].append((heights[near], idx))
            
        min_heap = []

        # iterate through building idx
        for far in range(n):
            
            # and for building that has deferred queries,
            # we push it onto a min heap
            for dq in deferred[far]:
                heapq.heappush(min_heap, dq)
                
            # see if the curr. building height could be greater
            # than the smallest height of any deferred queries in heap
            while min_heap and heights[far] > min_heap[0][0]:
                ans[min_heap[0][1]] = far
                heapq.heappop(min_heap)
                
        return ans

heights, queries = [6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]
heights, queries = [5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]]
heights, queries = [2,3,1], [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
heights, queries = [3,4,1,2], [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]

Solution().leftmostBuildingQueries(heights, queries)