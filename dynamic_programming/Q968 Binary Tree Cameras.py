# dp - hard
from functools import cache
from typing import Optional
class Solution:
    def minCameraCover(self, root: Optional["TreeNode"]) -> int:

        fmin = lambda a, b: a if a <= b else b

        @cache
        def f(node:Optional["TreeNode"], flag: bool) -> int:
            '''
            flag status:
            0 = not monitored at all (from parent's perspective);
            1 = no camera installed, but monitored;
            2 = camera installed and thus monitored
            '''

            # leaf node
            if not node.left and not node.right:
                return [1, 0, 1][flag]
            
            # when curr. node is not monitored, we could install a camera
            # at this node OR rely on its immediate child(ren)'s installation
            if flag == 0:

                # get relevant dfs results
                if node.left:
                    l = [f(node.left, 0), f(node.left, 1), f(node.left, 2)]
                if node.right:
                    r = [f(node.right, 0), f(node.right, 1), f(node.right, 2)]

                install = 1
                if node.left:
                    install += fmin(l[1], l[2])
                if node.right:
                    install += fmin(r[1], r[2])

                if node.left and node.right:
                    skip = fmin(l[2] + r[0], l[0] + r[2])
                elif node.left:
                    skip = l[2]
                elif node.right:
                    skip = r[2]

                return fmin(install, skip)

            # no camera to install, so only skip option
            elif flag == 1:

                # get relevant dfs results - (state 1 is skipped)
                if node.left and node.right:
                    skip = fmin(f(node.left, 0), f(node.left, 2)) + \
                           fmin(f(node.right, 0), f(node.right, 2))
                elif node.left:
                    skip = fmin(f(node.left, 0), f(node.left, 2))
                elif node.right:
                    skip = fmin(f(node.right, 0), f(node.right, 2))

                return skip
                
            # instructed to install camera, so only install option
            elif flag == 2:
                
                install = 1
                # get relevant dfs results - (state 0 is skipped)
                if node.left:
                    install += fmin(f(node.left, 1), f(node.left, 2))
                if node.right:
                    install += fmin(f(node.right, 1), f(node.right, 2))

                return install

        return f(root, 0)
    
root = [0]
root = [0,0,None,0,0]
root = [0,None,0,None,0,None,0]
root = [0,0,0,None,0,0,None,None,0]
root = [0,0,None,0,None,0,None,None,0]
root = [0,0,None,None,0,0,None,None,0,0]
root = [0,0,0,None,0,0,None,None,0,None,0,None,0,None,None,0,None,0,0]