# graph - hard
import heapq
class Solution: 
    def euclidean_dist(self, row, col):
        # make use of euclidean distance to break tie on cumuCost
        return (self.m-1-row) ** 2 + (self.n-1-col) ** 2

    def minCost(self, grid) -> int:
        
        # 1: to right, 2: to left, 3: to lower, 4: to upper
        # goal is to find min. cost to have at least one valid path, 
        # which does not have to be the shortest.

        self.m, self.n = len(grid), len(grid[0])

        bfs_queue = [[0,0,0,0]]
        visited = set()

        while bfs_queue:

            while (-bfs_queue[0][2], -bfs_queue[0][3]) in visited:
                heapq.heappop(bfs_queue)

            cumuCost, _, row, col = heapq.heappop(bfs_queue)
            row, col = -row, -col

            if row == self.m-1 and col == self.n-1:
                return cumuCost

            # mark visited
            visited.add((row, col))

            # visit the pointed cell first if valid
            if grid[row][col] == 1:
                if col+1 < self.n and (row, col+1) not in visited:
                    ed = self.euclidean_dist(row, col+1)
                    heapq.heappush(bfs_queue, [cumuCost, ed, -row, -(col+1)])

            if grid[row][col] == 2:
                if col-1 >= 0 and (row, col-1) not in visited:
                    ed = self.euclidean_dist(row, col-1)
                    heapq.heappush(bfs_queue, [cumuCost, ed, -row, -(col-1)])

            if grid[row][col] == 3:
                if row+1 < self.m and (row+1, col) not in visited:
                    ed = self.euclidean_dist(row+1, col)
                    heapq.heappush(bfs_queue, [cumuCost, ed, -(row+1), -col])

            if grid[row][col] == 4:
                if row-1 >= 0 and (row-1, col) not in visited:
                    ed = self.euclidean_dist(row-1, col)
                    heapq.heappush(bfs_queue, [cumuCost, ed, -(row-1), -col])

            # otherwise we have to incur a cost
            if col+1 < self.n and (row, col+1) not in visited:
                ed = self.euclidean_dist(row, col+1)
                heapq.heappush(bfs_queue, [cumuCost+1, ed, -row, -(col+1)])

            if row+1 < self.m and (row+1, col) not in visited:
                ed = self.euclidean_dist(row+1, col)
                heapq.heappush(bfs_queue, [cumuCost+1, ed, -(row+1), -col])

            if col-1 >= 0 and (row, col-1) not in visited:
                ed = self.euclidean_dist(row, col-1)
                heapq.heappush(bfs_queue, [cumuCost+1, ed, -row, -(col-1)])

            if row-1 >= 0 and (row-1, col) not in visited:
                ed = self.euclidean_dist(row-1, col)
                heapq.heappush(bfs_queue, [cumuCost+1, ed, -(row-1), -col])

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
grid = [[1,1,3],[3,2,2],[1,1,4]]
grid = [[1,2],[4,3]]

Solution().minCost(grid)