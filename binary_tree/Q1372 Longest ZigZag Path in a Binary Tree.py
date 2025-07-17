# binary tree - medium
class Solution:
    def longestZigZag(self, root) -> int:

        ans = 0
        def recursive_zigzag(node, direc, pathLen):

            nonlocal ans
            ans = max(ans, pathLen)
            if not node.left and not node.right:
                return
            
            if node.left:

                if direc in [0, -1]:
                    recursive_zigzag(node.left, 1, pathLen + 1)
                else:
                    recursive_zigzag(node.left, 1, 1)

            if node.right:

                if direc in [1, -1]:
                    recursive_zigzag(node.right, 0, pathLen + 1)
                else:
                    recursive_zigzag(node.right, 0, 1)

        recursive_zigzag(root, -1, 0)
        return ans