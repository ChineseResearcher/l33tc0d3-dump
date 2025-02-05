# binary tree - medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursiveBuild(self, currNode, lb, rb):

        currIdx = self.num_idx[currNode.val]

        # handle left
        if currIdx > lb:
            leftVal = max(self.nums[lb:currIdx])
            currNode.left = TreeNode(val=leftVal)
            self.recursiveBuild(currNode.left, lb, currIdx)

        # handle right
        if currIdx < rb-1:
            rightVal = max(self.nums[currIdx+1:rb])
            currNode.right = TreeNode(val=rightVal)
            self.recursiveBuild(currNode.right, currIdx+1, rb)

    def constructMaximumBinaryTree(self, nums):
        self.num_idx = {num: idx for idx, num in enumerate(nums)}
        n = len(nums)

        # every num in nums is unique
        # identify the root node, which is the max.
        rootVal = max(nums)
        root = TreeNode(val=rootVal)

        self.nums = nums
        self.recursiveBuild(root, 0, n)
        return root
    
nums = [2,3,1,6,0,5]
nums = [3,2,1]

Solution().constructMaximumBinaryTree(nums)