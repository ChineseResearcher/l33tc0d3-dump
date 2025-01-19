# graph - hard
import heapq 
class Solution:
    # it is extremely difficult to come up with the intuition that we should always
    # process the cell with min. boundary height. And if we try to precompute
    # maxHeight in cardinal directions like in TRW 1, it would fail on the 3rd TC provided
    # the key intuition is that by processing the next cell with the min. boundary height,
    # we are discovering the upper bound for water to trapped up to in an enclosed region
    # and there may be multiple enclosed regions in a given structure
    def trapRainWater(self, heightMap) -> int:
        
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

                    # find boundary height
                    lh = heightMap[r][c-1] if c-1 >= 0 else float('inf')
                    rh = heightMap[r][c+1] if c+1 < n else float('inf')
                    fh = heightMap[r-1][c] if r-1 >= 0 else float('inf')
                    bh = heightMap[r+1][c] if r+1 < m else float('inf')

                    boundary_height = max(min( min(lh, rh), min(fh, bh) ), heightMap[r][c])
                    heapq.heappush(min_heap, [boundary_height, r, c])

        ans = 0
        # perform BFS over min_heap         
        while min_heap:

            bdh, r, c = heapq.heappop(min_heap)

            # check in cardinal directions for un-visited neighbours
            if c-1 >= 0 and (r, c-1) not in visited:
                if bdh > heightMap[r][c-1]:
                    ans += bdh - heightMap[r][c-1]
                heapq.heappush(min_heap, [max(bdh, heightMap[r][c-1]), r, c-1])
                # because we've already accumulated trapped water for this neighbour cell
                # we need to mark visited to avoid multiple counting
                visited.add((r, c-1))

            if c+1 < n and (r, c+1) not in visited:
                if bdh > heightMap[r][c+1]:
                    ans += bdh - heightMap[r][c+1]
                heapq.heappush(min_heap, [max(bdh, heightMap[r][c+1]), r, c+1])
                visited.add((r, c+1))

            if r-1 >= 0 and (r-1, c) not in visited:
                if bdh > heightMap[r-1][c]:
                    ans += bdh - heightMap[r-1][c]
                heapq.heappush(min_heap, [max(bdh, heightMap[r-1][c]), r-1, c])
                visited.add((r-1, c))

            if r+1 < m and (r+1, c) not in visited:
                if bdh > heightMap[r+1][c]:
                    ans += bdh - heightMap[r+1][c]
                heapq.heappush(min_heap, [max(bdh, heightMap[r+1][c]), r+1, c])
                visited.add((r+1, c))

        return ans
    
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]

Solution().trapRainWater(heightMap)