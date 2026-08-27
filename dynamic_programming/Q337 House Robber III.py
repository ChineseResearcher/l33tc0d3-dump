# dp - medium
from functools import cache
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional['TreeNode']) -> int:

        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) tree DP with a state tracking rob status of parent

        @cache
        def f(node: Optional['TreeNode'], pr:bool) -> int:

            # we can always skip robbing curr. node
            skip = (f(node.left, False) if node.left else 0) + \
                   (f(node.right, False) if node.right else 0)

            # "pr" indicates if parent node has been robbed
            if not pr:
                rob_now = node.val + \
                          (f(node.left, True) if node.left else 0) + \
                          (f(node.right, True) if node.right else 0)
            else:
                rob_now = 0

            return fmax(skip, rob_now)

        return f(root, False)

root = [3,4,5,1,3,None,1]
root = [3,2,3,None,3,None,1]