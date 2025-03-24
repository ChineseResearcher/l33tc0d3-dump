# graph - medium
class Solution:
    def dfs(self, currNode, path, visited):
        # input is small, we could use backtracking to derive
        # all acylic paths from node 0 to node n-1

        if currNode == self.n-1:
            self.ans.append(path[::])
            return
        
        for neighbour in self.graph[currNode]:
            if neighbour not in visited:
                path.append(neighbour)
                visited.add(neighbour)
                self.dfs(neighbour, path, visited)
                # backtrack
                path.pop()
                visited.discard(neighbour)

    def allPathsSourceTarget(self, graph):
        self.n = len(graph)
        self.graph = graph

        self.ans = []
        _ = self.dfs(0, [0], set([0]))
        return self.ans
    
graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

Solution().allPathsSourceTarget(graph)