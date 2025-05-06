# graph - hard
from typing import List
class Solution:
    def dfs(self, curr):
    
        if curr in self.visited:
            return 0
        
        # mark visited
        self.visited.add(curr)
        
        for neighbour in self.couch_edges[curr]:
            if neighbour not in self.visited:
                return 1 + self.dfs(neighbour)
            
        return 0

    def minSwapsCouples(self, row: List[int]) -> int:
        _2N = len(row)
        # imagine a couch fitting two persons and for n couples we would
        # have n couches, and mark the couch that a person belongs to initially
        couchID = dict()

        for i in range(_2N):
            couchID[row[i]] = i // 2
            
        couch_edges = {i:set() for i in range(_2N // 2)}
        # draw an edge between a pair of couches if a couple is seated separately
        for i in range(0, _2N, 2):
            if couchID[i] != couchID[i+1]:
                couch_edges[couchID[i]].add(couchID[i+1])
                couch_edges[couchID[i+1]].add(couchID[i])

        self.couch_edges = couch_edges
        # after the couch-connections built, use a dfs visitor to find the
        # length of a cycle for each potential couch-group
        # Note: a couch is either not connected to any other couch
        # i.e. a couple already seated in the same couch OR a couch is connected
        # to two other couches because each of the seated person has their partner in another couch

        # maintain a visited set storing couches
        self.visited = set()
        
        ans = 0
        for couch in range(_2N // 2):
            if self.couch_edges[couch] and couch not in self.visited:
                ans += self.dfs(couch)

        return ans
    
row = [0,2,1,3]
row = [3,2,0,1]
row = [1,6,7,8,5,2,3,4,9,0]
row = [9,12,2,10,11,0,13,6,4,5,3,8,1,7]

Solution().minSwapsCouples(row)