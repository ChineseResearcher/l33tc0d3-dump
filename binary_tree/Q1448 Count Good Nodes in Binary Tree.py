# binary tree - medium
class Solution:
    def dfs(self, currNode, pathMax):
        # increment goodNodes w.r.t to the current pathMax
        if currNode.val >= pathMax:
            self.goodNodes += 1
            
        if currNode.left:
            self.dfs(currNode.left, max(currNode.val, pathMax))

        if currNode.right:
            self.dfs(currNode.right, max(currNode.val, pathMax))
        

    def goodNodes(self, root):

        # we track a pathMax variable as we dfs down the binary tree
        self.goodNodes = 0

        self.dfs(root, root.val)
        return self.goodNodes
    
root = [3,1,4,3,None,1,5]
root = [3,3,None,4,2]
root = [1]