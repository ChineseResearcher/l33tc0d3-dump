# graph - hard
from collections import defaultdict, deque
class Solution:
    def longestCycle(self, edges):

        # there are n nodes, with each node max. one outgoing edge
        n = len(edges)
        graph, indeg = defaultdict(list), defaultdict(int)

        for u, v in enumerate(edges):
            # absence of outgoing edge is marked by -1
            if v == -1:
                continue

            graph[u].append(v)
            indeg[v] += 1

        bfs_queue = deque([node for node in range(n) if indeg[node] == 0])
        # perform bfs-based topoSort
        topo = set()
        while bfs_queue:

            currNode = bfs_queue.popleft()
            topo.add(currNode)

            for neighbour in graph[currNode]:
                indeg[neighbour] -= 1
                if indeg[neighbour] == 0:
                    bfs_queue.append(neighbour)

        # nodes that do not appear in the topo set are node(s) involved in cycle(s)
        visit_order = dict()

        def cycle_length(currNode, order):

            # completes a cycle
            if currNode in visit_order:
                return order - visit_order[currNode]
            
            # mark visited with order
            visit_order[currNode] = order
            # move to next only neighbour
            if graph[currNode]:
                return cycle_length(graph[currNode][0], order+1)

        ans = -1
        for node in range(n):

            if node not in topo and node not in visit_order:
                ans = max(ans, cycle_length(node, 1))

        return ans
    
edges = [3,3,4,2,3]
edges = [2,-1,3,1]

Solution().longestCycle(edges)