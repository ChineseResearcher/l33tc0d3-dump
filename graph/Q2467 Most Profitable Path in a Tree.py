# graph - medium
from collections import deque
class Solution:
    def bob_path(self, currNode):
        # while Alice could reach diff. possible leaf nodes, the path that 
        # Bob takes is deterministic, i.e. only one path from node Bob to node 0

        # Bob reached node 0, and stop
        if currNode == 0:
            return [0]

        # mark visited
        self.visited.add(currNode)

        path = [currNode]
        # visit neighbour tree node
        for neighbour in self.e[currNode]:

            if neighbour not in self.visited:
                res = self.bob_path(neighbour)

                # two valid cases:
                # 1) already found valid path gets returned
                # 2) just reached node 0
                if len(res) > 1 or (len(res) == 1 and res[0] == 0):
                    path.extend(res)
                    return path
                
        return [-1]

    def mostProfitablePath(self, edges, bob, amount):
        
        n = len(amount)
        # create edges
        self.e = {i:[] for i in range(n)}
        for n1, n2 in edges:
            self.e[n1].append(n2)
            self.e[n2].append(n1)

        # maintain visited
        self.visited = set()

        # track the bob's deterministic path, with the order of visit stored
        bob_nodes = {node:idx for idx, node in enumerate(self.bob_path(bob))}

        # perform bfs search for Alice's decision paths
        # storing <currNode, order_of_visit, net_val>
        alice_path = deque([[0, 0, amount[0]]])

        # refresh visited, with node 0 already visited
        self.visited = set([0])

        ans = float('-inf')
        while alice_path:

            currNode, visitOrder, netVal = alice_path.popleft()

            # maintain a boolean to check if a leaf node is reached
            reachLeaf = True
            # explore neighbours
            for neighbour in self.e[currNode]:

                if neighbour not in self.visited:
                    
                    reachLeaf = False
                    self.visited.add(neighbour)

                    # scenario 1: no change to netval
                    if neighbour in bob_nodes and visitOrder+1 > bob_nodes[neighbour]:
                        alice_path.append([neighbour, visitOrder+1, netVal])

                    # scenario 2: node's award/cost fully taken by alice
                    if neighbour not in bob_nodes or (neighbour in bob_nodes and visitOrder+1 < bob_nodes[neighbour]):
                        alice_path.append([neighbour, visitOrder+1, netVal + amount[neighbour]])

                    # scenario 3: node's award/cost half taken by alice
                    if neighbour in bob_nodes and visitOrder + 1 == bob_nodes[neighbour]:
                        alice_path.append([neighbour, visitOrder+1, netVal + amount[neighbour]/2])

            if reachLeaf: ans = max(ans, netVal)

        return int(ans)
    
edges, bob, amount = [[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]
edges, bob, amount = [[0,1]], 1, [-7280,2350]
edges, bob, amount = [[0,2],[1,4],[1,6],[2,4],[3,6],[3,7],[5,7]], 4, [-6896,-1216,-1208,-1108,1606,-7704,-9212,-8258]

Solution().mostProfitablePath(edges, bob, amount)