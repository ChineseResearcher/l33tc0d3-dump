# binary tree - medium
from typing import Optional
class Solution:
    def maxProduct(self, root: Optional["TreeNode"]) -> int:

        MOD = int(1e9 + 7)
        # remember the subtree sum
        subtr_sum = dict()
        
        # dfs to return the sum of values in each subtree
        def f(curr: Optional["TreeNode"]) -> int:

            curr_sum = curr.val
            if curr.left:
                curr_sum += f(curr.left)
            if curr.right:
                curr_sum += f(curr.right)

            # memoize the sum
            subtr_sum[curr] = curr_sum
            return curr_sum

        # obtain sum for the entire binary tree
        all_sum = f(root)

        fmax = lambda a, b: a if a > b else b
        ans = 0
        for _, val in subtr_sum.items():
            split_prod = val * (all_sum - val)
            ans = fmax(ans, split_prod)

        return ans % MOD
    
root = [1,2,3,4,5,6]
root = [1,None,2,3,4,None,None,5,6]