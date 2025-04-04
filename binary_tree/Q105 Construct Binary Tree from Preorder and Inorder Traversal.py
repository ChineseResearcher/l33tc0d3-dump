# binary tree - medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        # first create two dicts storing the preorder/inorder elements with idx
        poi = {node: idx for idx, node in enumerate(preorder)}
        ioi = {node: idx for idx, node in enumerate(inorder)}

        # create a dict of nodes for all nodes given
        node_dict = {node: TreeNode(node) for node in preorder}

        # maintain a set tracking nodes with parent found
        hasParent = set()

        # we need two passes through preorder & inorder respectively
        # to locate the left & right child relations
        for i in range(n-1):

            # confirm if node preorder[i+1] is the left child of preorder[i]
            if ioi[preorder[i+1]] < ioi[preorder[i]]:
                node_dict[preorder[i]].left = node_dict[preorder[i+1]]
                hasParent.add(preorder[i+1])

        for j in range(n-1):

            # confirm if node inorder[j+1] is the right child of inorder[j]
            if inorder[j+1] not in hasParent and poi[inorder[j+1]] > poi[inorder[j]]:
                node_dict[inorder[j]].right = node_dict[inorder[j+1]]
                hasParent.add(inorder[j+1])

        # there might be unassigned right children after above two passes
        for k, node in node_dict.items():
            if k not in hasParent:
                # locate potential parent to left of node's position in inorder array
                for i in range(ioi[k]-1, -1, -1):
                    if poi[inorder[i]] < poi[k]:
                        node_dict[inorder[i]].right = node
                        break

        # the first node in preorder is always the root
        return node_dict[preorder[0]]
    
preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
preorder, inorder = [3,9,4,20,15,7], [9,4,3,15,20,7]