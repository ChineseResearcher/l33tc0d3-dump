# binary tree - medium
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        pc, self.lc, self.rc = 0, 0, 0
        # dfs helper to compute the count of nodes from parent's
        # direction, left & right child's direction

        def dfs(currNode):

            curr_cnt = 1

            l = 0
            if currNode.left:
                l = dfs(currNode.left)
                curr_cnt += l

            r = 0
            if currNode.right:
                r = dfs(currNode.right)
                curr_cnt += r
            
            if currNode.val == x:
                self.lc, self.rc = l, r
            
            return curr_cnt

        _ = dfs(root)
        
        pc = n - self.lc - self.rc - 1
        best = max(pc, max(self.lc, self.rc))
        return True if best > n - best else False
    
root, n, x = [1,2,3,4,5,6,7,8,9,10,11], 11, 3
root, n, x = [1,2,3], 3, 1
root, n, x = [1,2,3], 3, 2