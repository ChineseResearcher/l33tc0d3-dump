# binary search tree - medium
from typing import List, Optional
class Solution:
    def balanceBST(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        
        # key ideas:
        # 1) one-pass DFS to get all the node vals in sort them in asc. order
        # 2) since the question accepts any of the balanced search trees, we could
        # always attempt to build a BST where the root of curr. subtree is the median
        # val. of some range [l...r] assuming the underlying values are sorted

        # dfs helper
        def f(currNode: Optional[TreeNode]) -> List[int]:

            res = [currNode.val]
            if currNode.left:
                res.extend(f(currNode.left))
            if currNode.right:
                res.extend(f(currNode.right))

            return res

        all = sorted(f(root))

        n = len(all)
        def assign(l:int, r:int) -> Optional[TreeNode]:

            # invalid range
            if l > r:
                return None 
            
            mid = (l + r) // 2
            currNode = TreeNode(val=all[mid])
            currNode.left = assign(l, mid-1)
            currNode.right = assign(mid+1, r)

            return currNode

        return assign(0, n-1)
    
root = [2,1,3]
root = [1,None,2,None,3,None,4,None,None]
root = [1,None,15,14,17,7,None,None,None,2,12,None,3,9,None,None,None,None,11]