# graph - hard
from typing import List
from collections import defaultdict, deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        # build an underlying DAG by only considering edges going from a
        # number to a strictly larger number (i.e. a directed egde from 2 -> 3)
        graph = defaultdict(list)
        indeg = [ [0] * n for _ in range(m) ]

        # change in coordinates for accessing neighbours
        delta = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(m):
            for c in range(n):
                
                for dx, dy in delta:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                        graph[(r,c)].append((nr, nc))
                        indeg[nr][nc] += 1
                        
        # enqueue all cells with 0-indeg
        q = deque([(r,c,1) for r in range(m) for c in range(n) if indeg[r][c] == 0])

        # keep track of the length of path leading up to a cell
        lr = [ [0] * n for _ in range(m) ]
        for r, c, _ in q:
            lr[r][c] = 1
            
        ans = 0
        while q:
            
            r, c, dist = q.popleft()
            ans = max(ans, dist)
            
            for nr, nc in graph[(r,c)]:
                indeg[nr][nc] -= 1
                lr[nr][nc] = max(lr[nr][nc], dist)
                
                if indeg[nr][nc] == 0:
                    q.append((nr, nc, lr[nr][nc] + 1))
                    
        return ans
    
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,1,1]]

Solution().longestIncreasingPath(matrix)