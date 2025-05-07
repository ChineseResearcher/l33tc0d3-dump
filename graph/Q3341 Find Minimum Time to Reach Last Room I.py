# graph - medium
from typing import List
import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        m, n = len(moveTime), len(moveTime[0])
        # use a min-heap based bfs to find the min. time required to
        # go from (0,0) to (m-1, n-1)
        minTime = {(i,j):float('inf') for i in range(m) for j in range(n)}

        # start at (0,0) and init. the minheap
        minheap = [[0, 0, 0]]
        minTime[(0,0)] = 0 # moveTime[0][0]

        while minheap:
            
            currTime, r, c = heapq.heappop(minheap)
            if currTime > minTime[(r,c)]:
                continue
                
            # explore cardinal directions
            if c+1 < n:
                newTime = max(currTime, moveTime[r][c+1]) + 1
                if newTime < minTime[(r,c+1)]:
                    minTime[(r,c+1)] = newTime
                    heapq.heappush(minheap, [newTime, r, c+1])
                    
            if c-1 >= 0:
                newTime = max(currTime, moveTime[r][c-1]) + 1
                if newTime < minTime[(r,c-1)]:
                    minTime[(r,c-1)] = newTime
                    heapq.heappush(minheap, [newTime, r, c-1])
                    
            if r+1 < m:
                newTime = max(currTime, moveTime[r+1][c]) + 1
                if newTime < minTime[(r+1,c)]:
                    minTime[(r+1,c)] = newTime
                    heapq.heappush(minheap, [newTime, r+1, c])
                    
            if r-1 >= 0:
                newTime = max(currTime, moveTime[r-1][c]) + 1
                if newTime < minTime[(r-1,c)]:
                    minTime[(r-1,c)] = newTime
                    heapq.heappush(minheap, [newTime, r-1, c])
                    
        return minTime[(m-1,n-1)]
    
moveTime = [[0,4],[4,4]]
moveTime = [[0,0,0],[0,0,0]]
moveTime = [[0,1],[1,2]]
moveTime = [[56,93],[3,38]]

Solution().minTimeToReach(moveTime)