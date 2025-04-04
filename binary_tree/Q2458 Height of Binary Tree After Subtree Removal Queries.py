# binary tree - hard
from collections import deque
class Solution:
    def dfsBinaryTree(self, currNode):
        key = currNode.val
        leftDepth, rightDepth = 0, 0
        if currNode.left:
            leftDepth = self.dfsBinaryTree(currNode.left)
        if currNode.right:
            rightDepth = self.dfsBinaryTree(currNode.right)
            
        self.subTreeHeight[key] = max(leftDepth, rightDepth)
        return 1 + max(leftDepth, rightDepth)

    def bfsBinaryTree(self, currNode):
        bfs_queue = deque([[currNode, 0]])
        while bfs_queue:
            
            currItem = bfs_queue.popleft()
            currNode, currLvl = currItem[0], currItem[1]
            
            if currLvl not in self.level_dict:
                self.level_dict[currLvl] = [currNode.val]
            else:
                self.level_dict[currLvl].append(currNode.val)
                
            if currNode.left:
                bfs_queue.append([currNode.left, currLvl+1])
            if currNode.right:
                bfs_queue.append([currNode.right, currLvl+1])

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        self.subTreeHeight = dict() # storing <node_val, height of its subtree>
        self.level_dict = dict() # storing <level, list of nodes (val) at this level>

        _ = self.dfsBinaryTree(root)
        self.bfsBinaryTree(root)

        level_max_info = dict()
        for lvl, nodes in self.level_dict.items():
            
            if len(nodes) > 1:
                sub_heights = [self.subTreeHeight[node] for node in nodes]

                first_max, first_max_node = -1, None
                for i in range(len(nodes)):
                    if sub_heights[i] > first_max:
                        first_max, first_max_node = sub_heights[i], nodes[i]
                
                second_max, second_max_node = -1, None
                for j in range(len(nodes)):
                    if sub_heights[j] > second_max and nodes[j] != first_max_node:
                        second_max, second_max_node = sub_heights[j], nodes[j]
                        
                level_max_info[lvl] = [[first_max_node, first_max], [second_max_node, second_max]]

        ans_dict = dict()
        for lvl, nodes in self.level_dict.items():
            
            if len(nodes) == 1:
                ans_dict[nodes[0]] = max(lvl-1, 0)
                
            else:
                curr_lvl_max = level_max_info[lvl]
                first, second = curr_lvl_max[0], curr_lvl_max[1]
                
                first_max_node, first_max = first[0], first[1]
                second_max_node, second_max = second[0], second[1]
                for node in nodes:
                    
                    if node != first_max_node:
                        ans_dict[node] = first_max + lvl
                    else:
                        ans_dict[node] = second_max + lvl

        ans = []
        for q in queries:
            ans.append(ans_dict[q])

        return ans
    
root, queries = [1,3,4,2,None,6,5,None,None,None,None,None,7], [4]
root, queries = [5,8,9,2,1,3,7,4,6], [3,2,4,8]