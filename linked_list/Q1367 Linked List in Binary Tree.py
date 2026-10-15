# linked list - medium
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        
        # key ideas:
        # 1) DFS w/ a state pointing the curr. node in the linked list to be matched
        # 2) early terminate the DFS when there is a mismatch
        # 3) as the matched path might start at a non-root node, we
        # always need to explore the skip option for curr. tree node

        def f(tn: TreeNode, ln: ListNode, started: bool) -> bool:
            
            valMatch = (ln.val == tn.val)
            if valMatch and ln.next is None:
                return True

            if tn.left:
                if not started:
                    if f(tn.left, ln, started): return True
                if valMatch:
                    if f(tn.left, ln.next, True): return True

            if tn.right:
                if not started:
                    if f(tn.right, ln, started): return True
                if valMatch:
                    if f(tn.right, ln.next, True): return True

            return False

        return f(root, head, False)
    
head, root = [4,2,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
head, root = [1,4,2,6], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
head, root = [1,4,2,6,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]