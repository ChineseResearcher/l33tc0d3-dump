# graph - hard
from collections import deque
class Solution:
    # the biggest challenge is to see that to have valid answer the graph:
    # 1) needs to be bipartite
    # 2) to be bipartite it must not contain odd cycle
    def magnificentSets(self, n, edges) -> int:
        
        # build graph from bi-directed edges, or undirected edges
        # note that the underlying graph can be disconnected
        graph = [[] for _ in range(n+1)]

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        # it is important to realise that iff the graph is bipartite,
        # then there will be valid grouping possible. Here we use BFS
        # to detect any odd-cycle, which automatically fails bipartiteness
        colored = dict()

        # enqueue first node, color 0
        bfs_queue = deque([[1, 0]]) 
        colored[1] = 0
        while bfs_queue:

            currNode, color = bfs_queue.popleft()

            for neighbour in graph[currNode]:
                if neighbour in colored:
                    if colored[neighbour] == color:
                        return -1
                else:
                    # paint complement colour
                    colored[neighbour] = 1 - color
                    bfs_queue.append([neighbour, 1 - color])

        # after making sure the underlying graph is bipartite
        # we are guranteed to have some valid groupings and we use bfs we
        # find out the max. depth of each connected component and increment our ans
        grouping, componentDepth = dict(), dict()

        newestGrp = 0
        for node in range(1, n+1):

            if node not in grouping:
                newestGrp += 1
                currGrp = newestGrp
            else:
                currGrp = grouping[node]

            bfs_queue = deque([[node, 1]])
            # maintain a visited for each bfs search
            visited = set([node])
            while bfs_queue:

                currNode, currLvl = bfs_queue.popleft()
                # label group
                grouping[currNode] = currGrp

                for neighbour in graph[currNode]:
                    if neighbour not in visited:

                        # mark visited
                        visited.add(neighbour)

                        bfs_queue.append([neighbour, currLvl + 1])

            # as we bfs from every node (in every component)
            # we track the max. possible depth
            if currGrp not in componentDepth:
                componentDepth[currGrp] = currLvl
            else:
                componentDepth[currGrp] = max(componentDepth[currGrp], currLvl)

        return sum(componentDepth.values())
    
n, edges = 6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
n, edges = 3, [[1,2],[2,3],[3,1]]
n, edges = 6, [[1,3],[1,2],[3,4],[2,4],[2,5],[4,6],[5,6]]
n, edges = 41, [[15,9],[18,28],[16,23],[23,40],[4,10],[40,27],[32,35],[26,29],[29,38],[23,35],[15,10],[2,40],[16,24],[41,28],[12,6],[39,38],[6,10],[41,4],[21,41],[26,41],[20,17],[17,21],[24,5],[17,1],[6,27],[31,6],[16,7],[38,8]]

Solution().magnificentSets(n, edges)