# graph - medium
from typing import List
from collections import defaultdict, deque
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        for u, v in paths:
            g[u].append(v)
            g[v].append(u)

        # represent our final planting scheme
        ans = [-1] * n

        # global visited set
        visited = set()

        # create a bfs subroutine to plant according to the requirements
        def bfs(startNode):

            q = deque([startNode])
            visited.add(startNode)
            # assign plant type to startNode
            ans[startNode-1] = 1

            while q:

                curr = q.popleft()

                for neighbour in g[curr]:
                    if neighbour not in visited:

                        # query for available plants
                        avail = set([1,2,3,4]) - \
                                set([ans[x-1] for x in g[neighbour] if ans[x-1 != -1]])
                                
                        ans[neighbour-1] = avail.pop()
                        visited.add(neighbour)
                        q.append(neighbour)

        for garden in range(1, n+1):

            if garden not in visited:
                bfs(garden)

        return ans
    
n, paths = 3, [[1,2],[2,3],[3,1]]
n, paths = 4, [[1,2],[3,4]]
n, paths = 4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
n, paths = 5, [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]

Solution().gardenNoAdj(n, paths)