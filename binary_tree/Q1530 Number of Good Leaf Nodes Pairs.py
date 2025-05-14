# binary tree - medium
from typing import Optional
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        
        self.ans = 0
        def dfs(currNode):

            # reached leaf node
            if not currNode.left and not currNode.right:
                return [1]

            left_height = []
            if currNode.left:
                left_height.extend(dfs(currNode.left))

            right_height = []
            if currNode.right:
                right_height.extend(dfs(currNode.right))

            for x in left_height:
                for y in right_height:

                    if x + y <= distance:
                        self.ans += 1

            return [h+1 for h in left_height + right_height if h+1 < distance]

        _ = dfs(root)
        return self.ans
    
root, distance = [1,2,3,None,4], 3
root, distance = [1,2,3,4,5,6,7], 3
root, distance = [7,1,4,6,None,5,3,None,None,None,None,None,2], 3