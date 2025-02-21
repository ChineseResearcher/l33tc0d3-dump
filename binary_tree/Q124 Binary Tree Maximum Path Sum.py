# binary tree - hard
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive_max_path(self, currNode, currNodeIdx):

        # reached a leaf node
        if not currNode.left and not currNode.right:
            self.op4[currNodeIdx] = currNode.val
            return currNode.val
        
        # otherwise we have four options
        # op1: only take currNode itself
        op1 = currNode.val

        # op2 & 3: only take left or right node
        if currNode.left:
            op2= self.recursive_max_path(currNode.left, currNodeIdx * 2 + 1) 
        else:
            op2 = float('-inf')

        if currNode.right:
            op3 = self.recursive_max_path(currNode.right, currNodeIdx * 2 + 2)
        else:
            op3 = float('-inf')

        # op4: treat the currNode as the centre of path
        # and consider different combinations
        self.op4[currNodeIdx] = max(op1, max(op1+op2+op3, max(op1+op2, op1+op3)))

        return max(op1, max(op1+op2, op1+op3))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.op4 = dict()
        return max(self.recursive_max_path(root, 0), max(self.op4.values()))
    
# helper
def binaryTreeBuilder(elements: List[Optional[int]]) -> Optional[TreeNode]:
    '''
    Using BFS queue to store the active(not null) nodes to be 
    visited in order of queue, and assign left/right children to this active node
    '''
    if not elements or elements[0] is None:
        return None
    
    rootNode = TreeNode(val=elements[0])
    node_queue = deque([rootNode])
    
    # start from the second element
    i = 1  
    
    while i < len(elements):
        currentNode = node_queue.popleft()
        
        # Assign the left child
        if i < len(elements) and elements[i] is not None:
            leftNode = TreeNode(val=elements[i])
            currentNode.left = leftNode
            node_queue.append(leftNode)
        i += 1
        
        # Assign the right child
        if i < len(elements) and elements[i] is not None:
            rightNode = TreeNode(val=elements[i])
            currentNode.right = rightNode
            node_queue.append(rightNode)
        i += 1
    
    return rootNode

# testcases
rootNode = binaryTreeBuilder([1,2,3])
rootNode = binaryTreeBuilder([2,-1])
rootNode = binaryTreeBuilder([-2,-1])
rootNode = binaryTreeBuilder([-6,None,3,2])
rootNode = binaryTreeBuilder([8,9,-6,None,None,5,9])
rootNode = binaryTreeBuilder([-1,-2,10,-6,None,-3,-6])
rootNode = binaryTreeBuilder([-10,9,20,None,None,15,7])
rootNode = binaryTreeBuilder([5,4,8,11,None,13,4,7,2,None,None,None,1])
rootNode = binaryTreeBuilder([-1,None,9,-6,3,None,None,None,-2])

Solution().maxPathSum(rootNode)