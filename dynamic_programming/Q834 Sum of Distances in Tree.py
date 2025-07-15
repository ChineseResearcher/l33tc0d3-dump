# dp - hard
from typing import List
from collections import defaultdict 
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # init. dp arr. of length n storing the answer as to
        # the sum of distances to all node if we centre at node i
        dp = [0] * n

        # init. an additional arr. storing the size of subtree rooted at node i
        st_size = [1] * n

        # dfs process that assumes tree node 0 as the root
        # thus all edges are implied to be directed and pointed away from node 0
        def dfs_0(node, parent):

            for neighbour in g[node]:
                if neighbour != parent:

                    dfs_0(neighbour, node)
                    st_size[node] += st_size[neighbour]
                    dp[node] += dp[neighbour] + st_size[neighbour]

        def reRoot(x, y):

            # a key characteristic of re-root DP relies on 
            # re-rooting the tree from some root "x" to root "y"
            dp[x] -= dp[y] + st_size[y]
            st_size[x] -= st_size[y]

            dp[y] += dp[x] + st_size[x]
            st_size[y] += st_size[x]

        # modified dfs process that assumes rooted-at-node-0 problem
        # has been solved and now solves the sum of distances problem for other nodes
        def dfs_x(node, parent):

            # dp[node] as of now would be the solution if rooted at node
            # as we are reRooting and undoing reRoot in the dfs process, we need
            # to record dp[node] as the solution otherwise it would be unavailable after all
            ans[node] = dp[node]

            for neighbour in g[node]:
                if neighbour != parent:

                    # re-root from node to neighbour
                    reRoot(node, neighbour)

                    dfs_x(neighbour, node)

                    # undo re-root decision
                    reRoot(neighbour, node)

        dfs_0(0, -1)
        # after solving for root-0, init. the ans arr. from dp
        ans = [x for x in dp]

        # solve for node [1, n-1]
        dfs_x(0, -1)

        return ans
    
n, edges = 6, [[0,1],[0,2],[2,3],[2,4],[2,5]]
n, edges = 1, []
n, edges = 2, [[1,0]]

Solution().sumOfDistancesInTree(n, edges)