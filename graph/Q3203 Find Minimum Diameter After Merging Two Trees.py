# graph - hard
from collections import deque
import copy
class LC310:
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

    def findMinHeightTrees(self, edges):
        # determine n from edges:
        n = len(edges) + 1

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
        # the minimum height of tree and max. diameter of mht
        if len(ans) == 1:
            mht = self.dfs(ans[0], -1)
            d = mht * 2 - 2
            return mht, d

        mht1, mht2 = self.dfs(ans[0], -1), self.dfs(ans[1], -1)

        if mht1 == mht2:
            d = mht1 + (mht1 - 1) - 2
            return mht1, d
        elif mht1 < mht2:
            d = mht1 * 2 - 2
            return mht1, d
        else:
            d = mht2 * 2 - 2
            return mht2, d

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        # LC310 solves for Minimum Height Tree (MHTs)
        # this problem can be seen as an extension of that
        mht1, d1 = LC310().findMinHeightTrees(edges1)
        mht2, d2 = LC310().findMinHeightTrees(edges2)

        return max(mht1 + mht2 - 1, max(d1, d2))
    
edges1, edges2 = [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]]
edges1, edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Solution().minimumDiameterAfterMerge(edges1, edges2)