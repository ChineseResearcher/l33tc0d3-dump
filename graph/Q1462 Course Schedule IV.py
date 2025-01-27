# graph - medium
class Solution:
    def dfs(self, rootNode, currNode):
        
        # there could be multiple paths from the same rootNode to an intermediate node
        # but we don't need to continue dfs if we've reached a node where it's verified to be reachable
        if self.isReachable[rootNode][currNode]:
            return

        # mark reachable
        self.isReachable[rootNode][currNode] = True

        # reach a node where there's no more outgoing edges
        if not self.edges[currNode]:
            return
        
        for neighbour in self.edges[currNode]:
            self.dfs(rootNode, neighbour)

    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # idea is to dfs from each course (node) down to the furthest reachable node
        # and in this process, mark isReachable[i][j] True
        self.isReachable = [ [False] * numCourses for _ in range(numCourses)]

        # build graph
        self.edges = {i:[] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            self.edges[c1].append(c2)

        for i in range(numCourses):

            # dfs down every node, with node i as the rootNode
            self.dfs(i, i)

        ans = []
        for c1, c2 in queries:
            ans.append(self.isReachable[c1][c2])

        return ans
    
numCourses, prerequisites, queries = 2, [[1,0]], [[0,1],[1,0]]
numCourses, prerequisites, queries = 2, [], [[1,0],[0,1]]
numCourses, prerequisites, queries = 3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]

Solution().checkIfPrerequisite(numCourses, prerequisites, queries)