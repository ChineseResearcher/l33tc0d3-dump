# binary tree - medium
from collections import deque
class Solution:
    def minimumOperations(self, root):
        
        # goal is to make sure every level has been sorted
        # and count the minumum number of swaps to make it sorted

        # we can use BFS to traverse the tree and store the nodes in the level_dict

        level_dict = dict()
        bfs_queue = deque([[root, 0]])

        while bfs_queue:
            currItem = bfs_queue.popleft()
            currNode, currLvl = currItem[0], currItem[1]
            
            if currLvl not in level_dict:
                level_dict[currLvl] = [currNode.val]
            else:
                level_dict[currLvl].append(currNode.val)
                
            if currNode.left:
                bfs_queue.append([currNode.left, currLvl+1])
            if currNode.right:
                bfs_queue.append([currNode.right, currLvl+1])

        # then we can sort the nodes in each level and compare with the sorted nodes
        ans = 0
        for _, lvl_node_arr in level_dict.items():
            # since all node values are unique, we can construct a mapping
            val_idx = {val:idx for idx, val in enumerate(lvl_node_arr)}
            sorted_ref = sorted(lvl_node_arr)

            # if the value at lvl_node_arr[i] is not the same as sorted_ref[i]
            # we know swap is needed
            for i in range(len(lvl_node_arr)):
                if lvl_node_arr[i] != sorted_ref[i]:

                    ans += 1

                    # locate the swap indices
                    swap1, swap2 = i, val_idx[sorted_ref[i]]

                    # swap on lvl_node_arr
                    temp = lvl_node_arr[swap2]
                    lvl_node_arr[swap2] = lvl_node_arr[swap1]
                    lvl_node_arr[swap1] = temp

                    # update the val_idx
                    val_idx[lvl_node_arr[swap1]] = swap1
                    val_idx[lvl_node_arr[swap2]] = swap2

                    lvl_node_arr
                    
        return ans
    
root = [1,4,3,7,6,8,5,None,None,None,None,9,None,10]
root = [1,3,2,7,6,5,4]
root = [1,2,3,4,5,6]