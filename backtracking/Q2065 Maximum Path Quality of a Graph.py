# backtracking - hard
from typing import List
from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        # the problem can be summarised as:
        # what's the max. distinct sum of node values subject to
        # the condition that the sum of travelled edges (time) <= maxTime?

        # observe each edge weight (time) is at least 10,
        # and maxTime is at most 100, this is quite a loose constraint
        # meaning we could exhaust all possible routines as a path
        # would not exceed 10 stops anyways
        node_val = {i:val for i, val in enumerate(values)}

        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        ans = 0
        def backtrack(accTime, nodeSeq):

            nonlocal ans
            if accTime > maxTime:
                return
            
            if nodeSeq[-1] == 0:

                curr_res = 0
                for node in set(nodeSeq):
                    curr_res += node_val[node]
                ans = max(ans, curr_res)

            # continue visiting
            curr_node = nodeSeq[-1]
            for nextNode, tc in g[curr_node]:
                nodeSeq.append(nextNode)
                backtrack(accTime + tc, nodeSeq)
                # backtrack
                nodeSeq.pop()

        backtrack(0, [0])
        return ans
    
values, edges, maxTime = [0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49
values, edges, maxTime = [5,10,15,20], [[0,1,10],[1,2,10],[0,3,10]], 30
values, edges, maxTime = [1,2,3,4], [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], 50

Solution().maximalPathQuality(values, edges, maxTime)