# graph - hard
from typing import List
import heapq 
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m, n = len(heightMap), len(heightMap[0])

        # there's no need to precompute maxHeight in cardinal directions
        # we'll see how the effective boundary heights gets passed down

        min_heap = []
        visited = set()
        # start by pushing all boundary cells into our min-heap
        for r in range(m):
            for c in range(n):

                # check if boundary
                if r == 0 or r == m-1 or c == 0 or c == n-1:

                    # mark visited
                    visited.add((r, c))

                    # find bounding height of boundary cells
                    bdh = float('inf')
                    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n:
                            bdh = min(bdh, heightMap[nr][nc])

                    bdh = max(bdh, heightMap[r][c])
                    heapq.heappush(min_heap, [bdh, r, c])

        ans = 0
        # perform BFS over min_heap      
        while min_heap:

            bdh, r, c = heapq.heappop(min_heap)
            # crux of the algorithm: why does a minheap always
            # give the optimal (smallest) bounding height for a 3-d cell?
            # By building a minheap based on bounding heights, we ensure
            # that whenever we visit a new cell, the bounding height we pass down
            # is the smallest even though this cell might have other bounding heights

            # check in cardinal directions for un-visited neighbours
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:

                    if bdh > heightMap[nr][nc]:
                        ans += bdh - heightMap[nr][nc]

                    # why do we heappush even though the neighbour cell might be taller?
                    # because the taller neighbour cell can still possibly be a bounding height
                    # to some cells next to it (say cell A), and it we do not heappush, cells from other
                    # directions (of cell A) may impose a wrong (higher than actual) bounding height
                    # and thus causing overestimation of water held at cell A.
                    heapq.heappush(min_heap, [max(bdh, heightMap[nr][nc]), nr, nc])
                    visited.add((nr, nc))

        return ans
    
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
heightMap = [[2,2,2],[2,1,2],[2,1,2],[2,1,2]]
heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
heightMap = [[5,8,7,7],[5,2,1,5],[7,1,7,1],[8,9,6,9],[9,8,9,9]]

Solution().trapRainWater(heightMap)