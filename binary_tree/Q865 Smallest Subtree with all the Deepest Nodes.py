# binary tree - medium
from collections import deque
from typing import Optional
class Solution:
    def subtreeWithAllDeepest(self, root: Optional['TreeNode']) -> Optional['TreeNode']:

        # key ideas:
        # 1) use BFS traversal to get the level of the deepest nodes, and track
        # how many of them should exist in the binary tree

        # 2) use DFS to find the smallest subtree that 
        # would have all the deepest nodes in it

        q = deque([[root, 1]])

        # track deepest level and corresponding count
        dn_lvl, dn_cnt = 1, 0

        while q:

            curr, lvl = q.popleft()

            if lvl == dn_lvl:
                dn_cnt += 1
            elif lvl > dn_lvl:
                dn_lvl, dn_cnt = lvl, 1

            if curr.left:
                q.append([curr.left, lvl+1])
            if curr.right:
                q.append([curr.right, lvl+1])

        ans = None
        def f(curr: Optional['TreeNode'], lvl: int) -> int:

            nonlocal ans
            
            subtr_dn_cnt = 0
            if lvl == dn_lvl:
                subtr_dn_cnt += 1

            if curr.left:
                subtr_dn_cnt += f(curr.left, lvl+1)
            if curr.right:
                subtr_dn_cnt += f(curr.right, lvl+1)

            if ans is None and subtr_dn_cnt == dn_cnt:
                ans = curr

            return subtr_dn_cnt

        _ = f(root, 1)
        return ans
    
root = [1]
root = [0,1,3,None,2]
root = [3,5,1,6,2,0,8,None,None,7,4]