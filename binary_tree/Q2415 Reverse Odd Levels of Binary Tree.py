# binary tree - medium
from collections import deque
class Solution:
    def dfs(self, currNode, currLvl):
        # as we dfs down the binary tree, record the level elements in order
        if currLvl not in self.lvl_nodes:
            self.lvl_nodes[currLvl] = []
        
        self.lvl_nodes[currLvl].append(currNode.val)

        if currNode.left:
            self.dfs(currNode.left, currLvl+1)

        if currNode.right:
            self.dfs(currNode.right, currLvl+1)

    def reverseOddLevels(self, root):
        self.lvl_nodes = dict()
        self.dfs(root, 0)

        # after recording the level elements, use a BFS algorithm to reverse odd-level values
        bfs_queue = deque([root])
        currLvl, currLvlIdx = 0, 0
        
        while bfs_queue:

            isOdd = (currLvl % 2 == 1)

            currNode = bfs_queue.popleft()
            if currNode.left:
                bfs_queue.append(currNode.left)
            if currNode.right:
                bfs_queue.append(currNode.right)

            if isOdd:
                currNode.val = self.lvl_nodes[currLvl][-(currLvlIdx+1)]

            currLvlIdx += 1
            if currLvlIdx == 2 ** currLvl:
                currLvl += 1
                currLvlIdx = 0 # reset

        return root
    
root = [2,3,5,8,13,21,34]
root = [7,13,11]
root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]