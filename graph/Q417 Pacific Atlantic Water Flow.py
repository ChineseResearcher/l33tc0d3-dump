# graph - medium
from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        # first define all the edge cells that leak directly into ocean
        pacific, atlantic = [], []
        for c in range(n):
            pacific.append([0, c])
            atlantic.append([m-1, c])

        for r in range(m):
            pacific.append([r, 0])
            atlantic.append([r, n-1])

        # start a multisource-BFS from Pacific / Atlantic edge cells 
        def multi_bfs(source: List[List[int]]):

            q = deque(source)
            visited = set()
            for r, c in source:
                visited.add((r, c))

            while q:

                r, c = q.popleft()
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m) or not (0 <= nc < n):
                        continue 
                
                    if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        q.append([nr, nc])
                        visited.add((nr, nc))

            return visited

        common = multi_bfs(pacific) & multi_bfs(atlantic)
        return [[r, c] for r, c in common]
    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# constraint
heights = [[1] * 200 for _ in range(200)]

Solution().pacificAtlantic(heights)