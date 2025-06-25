# binary search tree - medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        # keep in mind this is BST, not generic binary tree
        # we should make use of the split property
        small, big = min(p.val, q.val), max(p.val, q.val)
        def dfs(curr):
            
            if small < curr.val < big or curr.val in [small, big]:
                self.ans = curr
                return

            if curr.val < small:
                dfs(curr.right)

            if curr.val > big:
                dfs(curr.left)

        _ = dfs(root)
        return self.ans
    
