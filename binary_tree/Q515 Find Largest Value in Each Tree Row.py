# binary tree - medium
from collections import deque
class Solution:
    def largestValues(self, root):
        # to find the largest value in each level of a binary tree
        # use BFS traversal to record the max. value as we visit each level

        if not root:
            return []

        bfs_queue = deque([(root, 0)])
        ans = []

        while bfs_queue:

            currNode, currLvl = bfs_queue.popleft()

            # if the current level is not in the ans list, add it
            if currLvl + 1 > len(ans):
                ans.append(float('-inf'))

            ans[currLvl] = max(ans[currLvl], currNode.val)

            if currNode.left:
                bfs_queue.append((currNode.left, currLvl+1))

            if currNode.right:
                bfs_queue.append((currNode.right, currLvl+1)) 

        return ans
    
root = [1,3,2,5,3,None,9]
root = [1,2,3]