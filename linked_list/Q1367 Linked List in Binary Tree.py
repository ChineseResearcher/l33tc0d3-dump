# linked list - medium
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfsFindStart(self, btNode):
        
        if btNode.val == self.head.val:
            self.entryPoints.append(btNode)

        if btNode.left:
            self.dfsFindStart(btNode.left)
        if btNode.right:
            self.dfsFindStart(btNode.right)

    def dfsMatchLL(self, llNode, btNode):   
        # value checking
        if llNode.val == btNode.val:
            if not llNode.next:
                print('match found')
                return True # complete ll match found
            llNode = llNode.next

            leftSearch, rightSearch = False, False

            if btNode.left:
                leftSearch = self.dfsMatchLL(llNode, btNode.left)
            if btNode.right:
                rightSearch = self.dfsMatchLL(llNode, btNode.right)

            # return true if either left or right has true returned
            return True if (leftSearch or rightSearch) else False
        
    def isSubPath(self, head, root) -> bool:
        self.head, self.root = head, root
        self.entryPoints = []
        # locate all nodes in the binary tree (bt) that matches the start of the linked list
        self.dfsFindStart(root)
        for ep in self.entryPoints:
            if self.dfsMatchLL(self.head, ep):
                return True
        return False
    
head, root = [4,2,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
head, root = [1,4,2,6], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
head, root = [1,4,2,6,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
head, root = [1,10], [1,None,1,10,1,9]
head, root = [2,2,1], [2,None,2,None,2,None,1]