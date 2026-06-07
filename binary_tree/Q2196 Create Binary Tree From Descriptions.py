# binary tree - medium
from typing import List, Optional
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional['TreeNode']:
        
        node_dict = dict() # <node, flag to indicate if assigned as child>
        for parent, child, isLeft in descriptions:

            if parent not in node_dict:
                node_dict[parent] = [TreeNode(val=parent), 0]
            p = node_dict[parent][0]

            if child not in node_dict:
                node_dict[child] = [TreeNode(val=child), 1]
            else:
                # update assign-child tag
                node_dict[child][1] = 1 
            c = node_dict[child][0]

            if isLeft:
                p.left = c
            else:
                p.right = c

        for v in node_dict.keys():
            if node_dict[v][1] == 0:
                return node_dict[v][0]
            
descriptions = [[1,2,1],[2,3,0],[3,4,1]]
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]