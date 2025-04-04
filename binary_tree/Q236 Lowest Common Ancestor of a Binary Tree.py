# binary tree - medium
class Solution:
    def recursiveSearch(self, currNode):
        # starting at the root node, dfs search left/right child if they exist
        # return True once p or q is found, return False once we exhaust nodes

        inLeft, inRight, inCurr = False, False, False
        if currNode.val in [self.p_val, self.q_val]:
            inCurr = True

        if currNode.left:
            inLeft = self.recursiveSearch(currNode.left)

        if currNode.right:
            inRight = self.recursiveSearch(currNode.right)

        # determine LCA: any of the following combinations would lead to LCA found
        # 1) inLeft = True, inRight = True
        # 2) inLeft = True, inCurr = True
        # 3) inRight = True, inCurr = True
        if sum([inLeft, inRight, inCurr]) == 2:
            self.lca = currNode

        return (inLeft or inRight or inCurr)

    def lowestCommonAncestor(self, root, p, q):
        self.lca = None
        self.p_val = p.val
        self.q_val = q.val

        self.recursiveSearch(root)

        # we will return the TreeNode instead of just the value of the node
        return self.lca
    
root, p, q = [3,5,1,6,2,0,8,None,None,7,4], 5, 1
root, p, q = [3,5,1,6,2,0,8,None,None,7,4], 5, 4
root, p, q = [1,2], 1, 2