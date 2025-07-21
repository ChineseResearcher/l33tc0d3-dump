# binary tree - medium
class Solution:
    def amountOfTime(self, root, start: int) -> int:
        # run DFS one time first to determine the max depth
        # from left and right child

        depth = dict()
        def dfs1(node):

            # make dict of dict for l/r
            # 0: left, 1: right
            depth[node.val] = {0:0, 1:0}

            if not node.left and not node.right:
                return 0
             
            if node.left:
                depth[node.val][0] = 1 + dfs1(node.left)

            if node.right:
                depth[node.val][1] = 1 + dfs1(node.right)

            return max(depth[node.val][0], depth[node.val][1])

        # compute l/r depth for non-leaf nodes
        _ = dfs1(root)

        # perform a second DFS to find the answer
        ans = max(depth[start][0], depth[start][1])

        def dfs2(node):
            
            nonlocal ans
            # keep dfs until we reach leafs or "start" node
            # at each level return the distance to "start" node
            # provided we have the "start" node in the subtree
            if node.val == start:
                return 1

            if not node.left and not node.right:
                return 0

            curr_res = 0
            if node.left:
                l_res = dfs2(node.left)
                if l_res > 0:
                    ans = max(ans, l_res + depth[node.val][1])

                curr_res = max(curr_res, l_res)

            if node.right:
                r_res = dfs2(node.right)
                if r_res > 0:
                    ans = max(ans, r_res + depth[node.val][0])

                curr_res = max(curr_res, r_res)

            return curr_res + 1 if curr_res > 0 else curr_res

        _ = dfs2(root)
        return ans