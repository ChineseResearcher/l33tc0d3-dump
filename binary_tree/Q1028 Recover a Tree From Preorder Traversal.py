# binary tree - hard

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive_recover(self, curr, expected_lvl):

        if self.node_idx == len(self.trvs_order)-1: return -1

        if self.trvs_order[self.node_idx+1][0] != expected_lvl+1:
            return self.node_idx+1
        
        # if left child is valid, assign directly
        # print(f'assigning left of {curr.val} to {trvs_order[node_idx+1][1]}')
        curr.left = TreeNode(val=self.trvs_order[self.node_idx+1][1])
        self.node_idx += 1

        # dfs down to find potential right child
        nn_idx = self.recursive_recover(curr.left, expected_lvl+1)
        if nn_idx > -1:
            if self.trvs_order[nn_idx][0] == expected_lvl + 1:
                # print(f'assigning right of {curr.val} to {trvs_order[nn_idx][1]}')
                curr.right = TreeNode(val=self.trvs_order[nn_idx][1])
                self.node_idx = nn_idx

                return self.recursive_recover(curr.right, expected_lvl+1)
                
        # print(f'returning nn_idx {nn_idx}, at lvl {expected_lvl}')
        return nn_idx

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # first convert traversal string into <level, num> pairs
        self.trvs_order = []

        dash_cnt, num_cache = 0, []
        for idx, char in enumerate(traversal):
            
            if char == '-' and traversal[idx-1] != '-':
                self.trvs_order.append([dash_cnt, int(''.join(num_cache))])
                # reset
                dash_cnt = 1 
                num_cache = []
                continue

            if char == '-': 
                dash_cnt += 1
            else:
                num_cache.append(char)

        # handle the last node
        self.trvs_order.append([dash_cnt, int(''.join(num_cache))])

        self.root = TreeNode(val=self.trvs_order[0][1])
        self.node_idx = 0

        _ = self.recursive_recover(self.root, 0)
        return self.root
    
traversal = "1-2--3--4-5--6--7"
traversal = "1-2--3---4-5--6---7"
traversal = "1-401--349---90--88"

Solution().recoverFromPreorder(traversal)