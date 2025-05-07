# dp - hard
from typing import List
from collections import defaultdict
class Solution:
    def recursive_visit(self, currNode, timeElapsed):
        # it's just strange that in order for memoization to give smallest
        # correct answer for each state, we must be able to visit predecessors

        # reached end node
        if currNode == self.n-1:
            return self.passingFees[self.n-1]
        
        if (currNode, timeElapsed) in self.dp:
            return self.dp[(currNode, timeElapsed)]

        curr_res = float('inf')
        for neighbour, tc in self.e[currNode].items():

            newTime = timeElapsed + tc
            if newTime <= self.maxTime:
                curr_res = min(curr_res, self.passingFees[currNode] + \
                                         self.recursive_visit(neighbour, newTime))

        self.dp[(currNode, timeElapsed)] = curr_res
        return curr_res

    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        e = defaultdict(dict)
        for x, y, t in edges:
            
            # de-dup repeated edges to speed up calculation
            # it's always optimal to use the smallest edge between two nodes
            if y not in e[x]:
                e[x][y] = float('inf')

            e[x][y] = min(e[x][y], t)

            if x not in e[y]:
                e[y][x] = float('inf')

            e[y][x] = min(e[y][x], t)

        # self.visited = [False] * len(passingFees)
        self.dp = dict()
        self.n, self.passingFees = len(passingFees), passingFees
        self.maxTime = maxTime
        self.e = e

        res = self.recursive_visit(0, 0)
        return res if res < float('inf') else -1
    
maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15],[2,4,1]]
passingFees = [5,1,2,20,20,3]

maxTime = 29
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]

maxTime = 25
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]

Solution().minCost(maxTime, edges, passingFees)