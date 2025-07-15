# binary tree - medium
class Solution:
    def distributeCoins(self, root) -> int:

        ans = 0
        def dfs(curr):
            
            nonlocal ans
            # the core idea to count the min. moves
            # is to consider the netflow at each tree node

            # netflow = the absolute diff between
            # 1) count of numbers in subtree rooted at "curr"
            # 2) sum of coin in subtree rooted at "curr"

            st_size, st_coin_sum = 1, curr.val
            if curr.left:
                size, coins = dfs(curr.left)
                st_size += size
                st_coin_sum += coins

            if curr.right:
                size, coins = dfs(curr.right)
                st_size += size
                st_coin_sum += coins

            ans += abs(st_size - st_coin_sum)
            return st_size, st_coin_sum

        _, _ = dfs(root)
        return ans