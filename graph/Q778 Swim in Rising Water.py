# graph - hard
import heapq
class Solution:
    # the concept to use BFS over min-heap is very similar to 
    # 407. Trapping Rain Water II, except that this is easier
    # without having to perform multi-source BFS
    def swimInWater(self, grid):
        
        m, n = len(grid), len(grid[0])
        # use BFS over min-heap, and track the max. height encountered
        # along the way until we reached grid[m][n]

        ans = 0

        # maintain visited
        visited = set()

        # queue stores <cell height, r, c>
        bfs_queue = [[grid[0][0], 0, 0]]
        while bfs_queue:

            height, r, c = heapq.heappop(bfs_queue)
            ans = max(ans, height)

            # if we reach bottom-right, early terminate
            if r == m-1 and c == n-1: break

            # otherwise continue explore cardinal directions
            if c+1 < n and (r, c+1) not in visited:
                heapq.heappush(bfs_queue, [grid[r][c+1], r, c+1])
                visited.add((r, c+1))

            if c-1 >= 0 and (r, c-1) not in visited:
                heapq.heappush(bfs_queue, [grid[r][c-1], r, c-1])
                visited.add((r, c-1))

            if r+1 < m and (r+1, c) not in visited:
                heapq.heappush(bfs_queue, [grid[r+1][c], r+1, c])
                visited.add((r+1, c))

            if r-1 >= 0 and (r-1, c) not in visited:
                heapq.heappush(bfs_queue, [grid[r-1][c], r-1, c])
                visited.add((r-1, c))

        return ans
    
grid = [[0,2],[1,3]]
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

Solution().swimInWater(grid)