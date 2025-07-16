# graph - medium
from collections import deque
import copy
class Solution:
    def dfs(self, currNode, parent):
        # dfs down every possible root assuming that every node i can be the root

        curr_depth = float('-inf') 
        for child_leaf in self.tc[currNode]:
            
            # make sure we don't go back to the parent
            if child_leaf != parent:
                curr_depth = max(curr_depth, self.dfs(child_leaf, currNode))

        # if we have no (valid) child leaves at all (i.e. reaching the end of the tree),
        # at least there is a depth of 1 to be returned
        return curr_depth + 1 if curr_depth != float('-inf') else 1

    def findMinHeightTrees(self, n, edges):
        # the idea is that the MHT can be formed if we root at the "centre of mass" of the tree
        # where the distances to and from the furthest leaf are minimized

        # an algorithm to arrive at such "centre of mass" (either 1 or 2) is to always
        # prune nodes with only one connection until there are only 1 or 2 nodes left

        tree_connect = {i:set() for i in range(n)}
        for i,j in edges:
            tree_connect[i].add(j)
            tree_connect[j].add(i)

        self.tc = copy.deepcopy(tree_connect)    

        bfs_queue = deque([node for node, children in tree_connect.items() if len(children) == 1])

        while bfs_queue:
            
            if len(tree_connect) <= 2:
                break
            currNode = bfs_queue.popleft()
            
            # delete for both directions
            assocNode = tree_connect[currNode].pop()
            del tree_connect[currNode]
            tree_connect[assocNode].discard(currNode)

            if len(tree_connect[assocNode]) == 1:
                bfs_queue.append(assocNode)

        ans = list(tree_connect.keys())
        # we need to validate if both nodes in ans are indeed MHTs
        # this can be verified by the diameter(height) computed from DFS

        # if ans only contains one node, direct return
        if len(ans) == 1:
            return ans

        d1, d2 = self.dfs(ans[0], -1), self.dfs(ans[1], -1)

        if d1 == d2:
            return ans
        elif d1 < d2:
            return [ans[0]]
        else:
            return [ans[1]]
    
n, edges = 4, [[1,0],[1,2],[1,3]]
n, edges = 6, [[3,0],[3,1],[3,2],[3,4],[5,4]]
n, edges = 2, [[0,1]]
n, edges = 1, []
n, edges = 9, [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[0,8]]

Solution().findMinHeightTrees(n, edges)