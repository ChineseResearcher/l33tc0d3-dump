# binary tree - medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # chain of thoughts is same as LC105, where preorder arr.
        # is replaced by postorder arr., and that postorder arr.
        # determines right child, inorder determines left child

        n = len(postorder)
        # first create two dicts storing the postorder/inorder elements with idx
        poi = {node: idx for idx, node in enumerate(postorder)}
        ioi = {node: idx for idx, node in enumerate(inorder)}

        # create a dict of nodes for all nodes given
        node_dict = {node: TreeNode(node) for node in postorder}

        # maintain a set tracking nodes with parent found
        hasParent = set()

        # we need two passes through postorder & inorder respectively
        # to locate the right & left child relations
        for i in range(n-1):

            # confirm if node postorder[i] is the right child of postorder[i+1]
            if ioi[postorder[i+1]] < ioi[postorder[i]]:
                node_dict[postorder[i+1]].right = node_dict[postorder[i]]
                hasParent.add(postorder[i])

        for j in range(n-1):

            # confirm if node inorder[j] is the left child of inorder[j+1]
            if inorder[j] not in hasParent and poi[inorder[j+1]] > poi[inorder[j]]:
                node_dict[inorder[j+1]].left = node_dict[inorder[j]]
                hasParent.add(inorder[j])

        # there might be unassigned left children after above two passes
        for k, node in node_dict.items():
            if k not in hasParent:
                # locate potential parent to left of node's position in inorder array
                for i in range(ioi[k]+1, n):
                    if poi[inorder[i]] > poi[k]:
                        node_dict[inorder[i]].left = node
                        hasParent.add(k)
                        break

        # root will be the only node without parent
        for k, node in node_dict.items():
            if k not in hasParent:
                return node
            
inorder, postorder = [9,3,15,20,7], [9,15,7,20,3]
inorder, postorder = [9,4,3,15,20,7], [4,9,15,7,20,3]