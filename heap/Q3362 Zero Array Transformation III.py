# heap - medium
from typing import List
import heapq
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n, m = len(nums), len(queries)
        # maintain a diff array
        diff = [0] * n

        # idea is to have the queries sorted by left bounds
        # and then as we iterate through nums, dynamically push valid queries to a maxheap
        queries.sort()

        h = []
        # maintain a pointer to access queries
        j = 0
        # maintain a running sum to track the number of times
        # nums[i] is being included in valid queries
        acc = 0

        for i in range(n):
            
            acc += diff[i]
            
            # enroll potential queries
            # what is potential? as long as a query's left bound includes i
            while j < m and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1
                
            while acc < nums[i] and h and abs(h[0]) >= i:
                r = heapq.heappop(h)
                # remember to make r +ve as the bound 
                # was inserted with -ve sign for a maxheap
                r = abs(r)
                
                # record the decrement of r+1 at diff
                if r+1 < n:
                    diff[r+1] -= 1
                
                # w/ every valid query applied, curr pos gets incremented
                acc += 1
                
            # if after exhausting all potential candidates from maxheap
            # acc still cannot match nums[i], then we say cannot convert to all 0s
            if acc < nums[i]:
                return -1
            
        # the number of queries left unused in the heap is the
        # number of queries we could have saved to turn arr to all 0s
        return len(h)
    
nums, queries = [2,0,2], [[0,2],[0,2],[1,1]]
nums, queries = [1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]
nums, queries = [1,2,3,4], [[0,3]]
nums, queries = [0,3], [[0,1],[0,0],[0,1],[0,1],[0,0]]
nums, queries = [0,0,1,1,0], [[3,4],[0,2],[2,3]]

Solution().maxRemoval(nums, queries)