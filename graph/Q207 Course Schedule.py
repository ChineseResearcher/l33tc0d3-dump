# graph - medium
class Solution:
    def dfs_check(self, pathNodes, currNode):
        # using a DFS algorithm, detect if there are any cycles
        # in the underlying represented graph as only DAG would avoid recurring dependencies
        
        # if no neighbours at all, we mark it as no cycle
        if not self.connections[currNode]:
            return False

        # mark visited
        self.visited[currNode] = True

        # add to pathNodes
        pathNodes = pathNodes.copy()
        pathNodes.add(currNode)

        # has_cycle boolean flag to change to True as long as 
        # any recursive result(s) return True
        has_cycle = False
        for dependent in self.connections[currNode]:
            if dependent in pathNodes:
                return True

            if not self.visited[dependent]:
                if self.dfs_check(pathNodes, dependent):
                    has_cycle = True

        return has_cycle

    def canFinish(self, numCourses, prerequisites) -> bool:
        
        self.visited = {i:False for i in range(numCourses)}
        self.connections = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            self.connections[p[1]].append(p[0]) # pre-req[1] -> pre-req[0]

        for i in range(numCourses):
            
            has_cycle = self.dfs_check(set(), i)

            if has_cycle:
                return False

        return True
    
numCourses, prerequisites = 2, [[1,0]]
numCourses, prerequisites = 2, [[1,0],[0,1]]
numCourses, prerequisites = 2, [[0,1]]
numCourses, prerequisites = 5, [[1,4],[2,4],[3,1],[3,2]]
numCourses, prerequisites = 3, [[1,0],[2,0],[0,2]]
numCourses, prerequisites = 7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

Solution().canFinish(numCourses, prerequisites)