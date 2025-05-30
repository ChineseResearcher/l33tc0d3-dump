# graph - medium
from typing import List
from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        # in this graph, there's only ONE outgoing edge from every node
        # and there may be cycle(s) in the graph

        n = len(edges)

        # perform two dfs starting from node1/2 each
        # and collect the distance info as we visit nodes
        def get_dist(node):

            dist = defaultdict(int)
            def dfs(node, currDist):
                
                # mark dist
                dist[node] = currDist
                # if revisit happens
                if edges[node] in dist:
                    return
                
                # if dead end
                if edges[node] == -1:
                    return
                
                dfs(edges[node], currDist+1)

            _ = dfs(node, 0)
            return dist

        d1, d2 = get_dist(node1), get_dist(node2)
        # for all the common visit nodes, compare the max, and minimise it
        ans, best_dist = -1, float('inf')

        for node in range(n):

            if node in d1 and node in d2:
                curr = max(d1[node], d2[node])

                # we only want the smallest index in case of multiple answers
                if curr < best_dist:
                    ans = node
                    best_dist = curr

        return ans
    
edges, node1, node2 = [2,2,3,-1], 0, 1
edges, node1, node2 = [1,2,-1], 0, 2

Solution().closestMeetingNode(edges, node1, node2)