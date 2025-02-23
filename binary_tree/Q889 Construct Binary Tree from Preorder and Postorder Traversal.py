# binary tree - medium
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        # two dicts to track the pos. of preorder/postorder distinct
        # numbers in their respective arr.
        pre_pos, post_pos = dict(), dict()
        for i in range(n):
            pre_pos[preorder[i]] = i
            post_pos[postorder[-(i+1)]] = n-i-1

        # maintain a dict to indicate the status of an incoming edge
        inEdge = {num: False for num in preorder}

        # initiate the TreeNodes for every appeared distinct num
        tn = {num: TreeNode(val=num) for num in preorder}

        # first process the pre-ordered seq.
        for i in range(1, n):

            if post_pos[preorder[i]] < post_pos[preorder[i-1]]:
                # create the left link
                tn[preorder[i-1]].left = tn[preorder[i]]
                # mark inEdge status to True
                inEdge[preorder[i]] = True

        # another one-pass thru. post-ordered seq.
        for i in range(n-2, -1, -1):

            if not inEdge[postorder[i]] and pre_pos[postorder[i]] > pre_pos[postorder[i+1]]:
                if tn[postorder[i+1]].left:
                    tn[postorder[i+1]].right = tn[postorder[i]]
                else:
                    tn[postorder[i+1]].left = tn[postorder[i]]
                # mark inEdge for debug too
                inEdge[postorder[i]] = True
        
        # root is always the first element in preorder traversal
        return tn[preorder[0]]
    
preorder, postorder = [1,2,4,5,6,3,7,8], [4,6,5,2,7,8,3,1]
preorder, postorder = [1,2,4,5,3,6,7], [4,5,2,6,7,3,1]
preorder, postorder = [1], [1]

Solution().constructFromPrePost(preorder, postorder)