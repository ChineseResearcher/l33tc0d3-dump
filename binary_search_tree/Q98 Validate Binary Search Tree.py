# bst - medium
class Solution:
    def dfs(self, currNode, curr_lb, curr_rb):
        # we need curr left/right bound to be updated as we dfs

        if not currNode.left and not currNode.right:
            return True

        left_res = True
        if currNode.left:

            if currNode.val <= currNode.left.val:
                return False
            if currNode.left.val <= curr_lb or currNode.left.val >= curr_rb:
                return False

            # right bound gets potentially tightened
            left_res = self.dfs(currNode.left, curr_lb, min(curr_rb, currNode.val))

        right_res = True
        if currNode.right:

            if currNode.val >= currNode.right.val:
                return False
            if currNode.right.val <= curr_lb or currNode.right.val >= curr_rb:
                return False

            # left bound gets potentially tightened
            right_res = self.dfs(currNode.right, max(curr_lb, currNode.val), curr_rb)

        return (left_res and right_res)

    def isValidBST(self, root):
        return self.dfs(root, float('-inf'), float('inf'))
    
root = [2,1,3]
root = [5,1,4,None,None,3,6]
root = [5,4,6,None,None,3,7]