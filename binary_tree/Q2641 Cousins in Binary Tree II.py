# binary tree - medium
from collections import deque
class Solution:
    def replaceValueInTree(self, root):
        
        currNode = root
        bfs_queue = deque([[currNode, 0]])

        # initiate a lvl_stat dictionary storing <lvl_num, [lvl_cnt, lvl_sum]>
        lvl_stat = dict()
        lvl_stat[0] = [1, currNode.val]
        # initiate a list storing the sibiling sum of the node in the order of traversal
        sibling_sum = deque([-1])

        while bfs_queue:

            currItem = bfs_queue.popleft()
            currNode, currLvl = currItem[0], currItem[1]

            childSum = 0
            if currNode.left:
                childSum += currNode.left.val
            if currNode.right:
                childSum += currNode.right.val

            # update lvl_stat
            if currLvl+1 not in lvl_stat:
                lvl_stat[currLvl+1] = [0,0]
            if childSum > 0: # indication of having child
                lvl_stat[currLvl+1][0] += 1
                lvl_stat[currLvl+1][1] += childSum
                
            # update sibling_sum & bfs_queue
            if currNode.left:
                bfs_queue.append([currNode.left, currLvl+1])
                sibling_sum.append(childSum)
            if currNode.right:
                bfs_queue.append([currNode.right, currLvl+1])
                sibling_sum.append(childSum)

        currNode = root
        bfs_queue = deque([[currNode, 0]])

        while bfs_queue:

            currItem = bfs_queue.popleft()
            currNode, currLvl = currItem[0], currItem[1]
            currSibSum = sibling_sum.popleft()

            if lvl_stat[currLvl][0] == 1:
                currNode.val = 0
            else:
                currNode.val = lvl_stat[currLvl][1] - currSibSum

            if currNode.left:
                bfs_queue.append([currNode.left, currLvl+1])
            if currNode.right:
                bfs_queue.append([currNode.right, currLvl+1])
        
        return root
    
root = [5,4,9,1,10,None,7]
root = [3,1,2]