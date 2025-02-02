# graph - medium
class Solution:
    # related to LC207 Course Schedule I but much stricter in the efficiency required to detect cycles
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
    
    def eventualSafeNodes(self, graph):

        # using dfs in this problem needs to be coupled with caching
        # in order to pass the time constraints
        n = len(graph)

        # 0: unvisited node, 1: safe node 2: unsafe node
        self.cache = [0] * n
        self.graph = graph
   
        return [node for node in range(n) if not self.has_cycle(node)]
    
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = [[1,2],[2],[]]

Solution().eventualSafeNodes(graph)