# dp - medium
from typing import List
from collections import defaultdict
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        # first build bi-directional graph, with dfs from root 0
        # to eliminate unnecessary connections afterwards
        g = defaultdict(set)

        for u, v in edges:

            g[u].add(v)
            g[v].add(u)
        
        self.g = g
        def dfs_trim(currNode):

            # depend on which node we start, the function
            # would trim edges such that a directed graph
            # from the starting node remains

            if not self.g[currNode]:
                return
            
            for neighbour in self.g[currNode]:
                self.g[neighbour].discard(currNode)
                dfs_trim(neighbour)

        _ = dfs_trim(0)

        # with the trimmed graph, now it is a directed tree
        # we would use a recursive dp to address subproblem related to subtrees
        def recursive_op(currNode):

            # goal of our function is to return the min. sum of
            # node values to keep untouched so that the rest of nodes can
            # all be used for accumulation of scores
            if not self.g[currNode]:
                return values[currNode]
            
            if currNode in dp:
                return dp[currNode]
            
            curr_ans = 0
            for neighbour in self.g[currNode]:
                curr_ans += recursive_op(neighbour)

            # either we keep best min. from subtrees rooted at children
            # or we use currNode's value is the min.
            curr_ans = min(curr_ans, values[currNode])
            dp[currNode] = curr_ans

            return curr_ans

        dp = dict()
        return sum(values) - recursive_op(0)
    
edges, values = [[0,1],[0,2],[0,3],[2,4],[4,5]], [5,2,5,2,1,1]
edges, values = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [20,10,9,7,4,3,5]

Solution().maximumScoreAfterOperations(edges, values)