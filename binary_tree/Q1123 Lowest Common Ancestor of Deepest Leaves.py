# binary tree - medium
class Solution:
    def find_lca(self, currNode, currLevel):
        # we could design a dfs algorithm to track
        # the deepest leaves and return its parent

        if not currNode.left and not currNode.right:
            # note: the lca of one node is itself
            if self.parent[currNode].left and self.parent[currNode].right:
                return self.parent[currNode], currLevel
            else:
                return currNode, currLevel
        
        l_depth, r_depth = float('-inf'), float('-inf')
        if currNode.left:
            # mark parent
            self.parent[currNode.left] = currNode
            lca_left, l_depth = self.find_lca(currNode.left, currLevel+1)

        if currNode.right:
            # mark parent
            self.parent[currNode.right] = currNode
            lca_right, r_depth = self.find_lca(currNode.right, currLevel+1)

        if l_depth > r_depth:
            return lca_left, l_depth
        elif r_depth > l_depth:
            return lca_right, r_depth
        # if equal return the currNode
        else:
            return currNode, r_depth

    def lcaDeepestLeaves(self, root):
        self.parent = dict()
        # init. the parent of root to be root
        self.parent[root] = root
        ans, _ = self.find_lca(root, 0)

        return ans
    
root = [3,5,1,6,2,0,8,None,None,7,4]
root = [1,2,None,3,4,None,6,None,5]
root = [0,1,3,None,2]