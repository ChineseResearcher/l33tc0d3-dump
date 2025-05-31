# binary tree - hard
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Codec:

    # idea is to perform pre-order DFS traversal to record
    # the node values (including Nulls) in a string
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def dfs(currNode):

            if not currNode.left and not currNode.right:
                return [str(currNode.val), 'n', 'n']
            
            currLvl = [str(currNode.val)]
            if currNode.left:
                left = dfs(currNode.left)
            else:
                left = ['n']

            if currNode.right:
                right = dfs(currNode.right)
            else:
                right = ['n']

            currLvl.extend(left)
            currLvl.extend(right)
            return currLvl
    
        # encode as string
        return '_'.join(dfs(root)) if root else ''
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # check for empty string
        if not data:
            return []

        nodeVals = data.split('_')

        st = [[TreeNode(val = int(nodeVals[0])), 2]]
        head = st[0][0]

        # pointer to reference nodeVals
        idx = 1

        while idx < len(nodeVals):

            if not st:
                st.append([TreeNode(val = int(nodeVals[idx])), 2])
            
            else:
                # assign left
                if st[-1][1] == 2:
                    st[-1][1] -= 1

                    if nodeVals[idx] != 'n':
                        st[-1][0].left = TreeNode(val = int(nodeVals[idx]))
                        st.append([st[-1][0].left, 2])

                elif st[-1][1] == 1:
                    
                    p_node, _ = st.pop()
                    if nodeVals[idx] != 'n':
                        p_node.right = TreeNode(val = int(nodeVals[idx]))
                        st.append([p_node.right, 2])

            idx += 1

        return head