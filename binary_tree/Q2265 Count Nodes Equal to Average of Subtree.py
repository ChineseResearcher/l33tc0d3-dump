# binary tree - medium
from typing import Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        ans = 0
        def f(currNode: TreeNode) -> Tuple[int, int]:
            
            nonlocal ans
            subtr_sum, subtr_cnt = currNode.val, 1
            if currNode.left:
                l_sum, l_cnt = f(currNode.left)
                subtr_sum += l_sum
                subtr_cnt += l_cnt

            if currNode.right:
                r_sum, r_cnt = f(currNode.right)
                subtr_sum += r_sum
                subtr_cnt += r_cnt

            subtr_avg = subtr_sum // subtr_cnt
            if currNode.val == subtr_avg:
                ans += 1

            return subtr_sum, subtr_cnt

        _ = f(root)
        return ans

root = [4,8,5,0,1,None,6]