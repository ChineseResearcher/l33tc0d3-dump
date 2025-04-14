# dp - medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive_build(self, start, end):

        # binary search tree should have smaller leaf on left
        # and larger leaf on right, this affects our formation

        # our states defined by start & end
        # e.g. (1,3) would refer to the subtree having nodes 1-3

        if end < start or start > end:
            return [None]
        
        if start == end:
            return [TreeNode(val=start)]
        
        if (start, end) in self.dp: return self.dp[(start, end)]

        curr_ans = []
        for root in range(start, end+1):
            
            # obtain left subtrees and right subtrees
            lst = self.recursive_build(start, root-1)
            rst = self.recursive_build(root+1, end)

            # explore combinations
            for s1 in lst:
                for s2 in rst:
                    # add to ans
                    curr_ans.append(TreeNode(val=root, left=s1, right=s2))

        self.dp[(start, end)] = curr_ans
        return curr_ans

    def generateTrees(self, n: int):
        self.dp = dict()
        return self.recursive_build(1,n)

n = 12 # code is efficient up to n = 12
n = 3

Solution().generateTrees(n)