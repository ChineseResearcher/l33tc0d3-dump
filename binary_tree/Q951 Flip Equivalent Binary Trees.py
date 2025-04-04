# binary tree - medium
from collections import deque
class Solution:
    def bfs_traversal(self, root):
        
        hierachy = dict()
        bfs_queue = deque([root])
        while bfs_queue:

            currNode = bfs_queue.popleft()
            hierachy[currNode.val] = []

            left_val, right_val = None, None
            if currNode.left:
                left_val = currNode.left.val
                bfs_queue.append(currNode.left)
            if currNode.right:
                right_val = currNode.right.val
                bfs_queue.append(currNode.right)

            if left_val and right_val:
                if left_val <= right_val:
                    hierachy[currNode.val].extend([left_val, right_val])
                else:
                    hierachy[currNode.val].extend([right_val, left_val])
            else:
                if left_val:
                    hierachy[currNode.val].append(left_val)
                if right_val:
                    hierachy[currNode.val].append(right_val)

        return hierachy

    def flipEquiv(self, root1, root2):
        
        # question assumes unique node values, which simplifies the problem
        # we just have to traverse the tree and construct a dictionary storing <parent_node_val: child_node_val>
        # and compare both trees to see if they are structurally equivalent

        hierachy1 = self.bfs_traversal(root1) if root1 else dict()
        hierachy2 = self.bfs_traversal(root2) if root2 else dict()

        return hierachy1 == hierachy2
    
root1 = [1,2,3,4,5,6,None,None,None,7,8]
root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]