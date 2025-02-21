# binary tree - medium
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        # rectify the contaminated root node to 0
        root.val = 0

        self.nodeVals = set([0])

        # initialise a bfs queue to rectify all remaining nodes
        bfs_queue = deque([root])

        while bfs_queue:

            curr = bfs_queue.popleft()

            if curr.left:
                curr.left.val = 2 * curr.val + 1
                bfs_queue.append(curr.left)
                self.nodeVals.add(curr.left.val)
            
            if curr.right:
                curr.right.val = 2 * curr.val + 2
                bfs_queue.append(curr.right)
                self.nodeVals.add(curr.right.val)
        
    def find(self, target: int) -> bool:
        return True if target in self.nodeVals else False
    
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
rootNode = binaryTreeBuilder([-1,None,-1])
obj = FindElements(rootNode)

commands = ["find","find"]
arguments = [[1],[2]]

rootNode = binaryTreeBuilder([-1,-1,-1,-1,-1])
obj = FindElements(rootNode)

commands = ["find","find","find"]
arguments = [[1],[3],[5]]

rootNode = binaryTreeBuilder([-1,None,-1,-1,None,-1])
obj = FindElements(rootNode)

commands = ["find","find","find","find"]
arguments = [[2],[3],[4],[5]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))