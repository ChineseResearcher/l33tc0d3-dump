# graph - medium
from collections import deque
class Solution:
    def has_cycle(self, node):
        # for every node we run this dfs-based cycle checker

        # return memoized result
        if self.cache[node] == -1:
            return True
        if self.cache[node] == 1:
            return False
        
        # first mark currNode as unsafe until proven otherwise
        self.cache[node] = -1
        for neighbor in self.graph[node]:
            if self.has_cycle(neighbor):
                return True
        
        # after recursively checking on every neighbour and no cycle is detected
        # re-flag the currNode's status to 1: indicating a safe node
        self.cache[node] = 1
        return False

    def findOrder(self, numCourses, prerequisites):
        # special case: no pre-requisites
        if not prerequisites: return list(range(numCourses))

        # maintain inDeg for bfs topoSort later
        inDeg = {i:0 for i in range(numCourses)}

        # build graph
        self.graph = {i:[] for i in range(numCourses)}
        for n1, n2 in prerequisites:
            self.graph[n2].append(n1) # directed edge

            inDeg[n1] += 1

        # as implied by the question, there can be cycle in the represented graph
        # use dfs+caching to detect cycles
        self.cache = [0] * numCourses
        for node in range(numCourses):
            if self.has_cycle(node):
                return []

        # if no cycle detected, derive the topological order using BFS (Kahn's algorithm)
        # enqueue all nodes with no incoming edges
        bfs_queue = deque([k for k,v in inDeg.items() if v == 0])

        ans = [] # our ans is the topologically ordered nodes
        while bfs_queue:

            currNode = bfs_queue.popleft()
            ans.append(currNode)

            # bfs visit neighbour
            for neighbour in self.graph[currNode]:
                inDeg[neighbour] -= 1
                if inDeg[neighbour] == 0:
                    bfs_queue.append(neighbour)

        return ans

numCourses, prerequisites = 2, [[1,0]]
numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
numCourses, prerequisites = 3, [[0,1],[1,2],[2,0]] # cycle case
numCourses, prerequisites = 3, [[0,1],[0,2],[1,2]]

Solution().findOrder(numCourses, prerequisites)