# binary tree - medium
from collections import deque, defaultdict
from typing import Optional
class Solution:
    def maxLevelSum(self, root: Optional['TreeNode']) -> int:

        # dict to recording level sum
        lvl_sum = defaultdict(int)
        
        q = deque([[root, 1]])
        while q:

            curr, lvl = q.popleft()
            lvl_sum[lvl] += curr.val

            if curr.left:
                q.append([curr.left, lvl+1])
            if curr.right:
                q.append([curr.right, lvl+1])

        ans, max_val = -1, float('-inf')
        # iterate through level sum
        lvl = 1
        while lvl in lvl_sum:

            if lvl_sum[lvl] > max_val:
                max_val = lvl_sum[lvl]
                ans = lvl

            lvl += 1

        return ans
    
root = [1,7,0,7,-8,None,None]
root = [989,None,10250,98693,-89388,None,None,None,-32127]