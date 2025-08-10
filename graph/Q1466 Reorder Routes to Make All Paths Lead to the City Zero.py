# graph - medium
from typing import List
class Solution:
    def dfs(self, currNode, visited):
        # mark visited
        next_visited = visited.copy()
        next_visited.add(currNode)

        for nb in self.neighbour[currNode]:
            if nb not in visited:

                # increment ans if the connection is currently
                # going from currNode to nb
                if self.isconnected[currNode][nb]:
                    self.ans += 1
                self.dfs(nb, next_visited)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # since there are only n-1 roads for n cities, 0-city is either at extreme end OR in the middle
        # we could use DFS to visit (if any) L/R direction of 0-city until we reach the end and compute the answer
        self.neighbour = {i: [] for i in range(n)}
        self.isconnected = [[False] * n for _ in range(n)]
        for x in connections:

            self.neighbour[x[0]].append(x[1])
            self.neighbour[x[1]].append(x[0])

            self.isconnected[x[0]][x[1]] = True

        # our number of reordered routes needed
        self.ans = 0

        self.dfs(0, set())
        return self.ans
    
n, connections = 3, [[0,1],[1,3],[2,3],[4,0],[4,5]]
n, connections = 5, [[1,0],[1,2],[3,2],[3,4]]
n, connections = 3, [[1,0],[2,0]]

Solution().minReorder(n, connections)