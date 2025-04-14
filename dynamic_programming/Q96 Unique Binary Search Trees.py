# dp - medium
class Solution:
    # there's another commit under Binary Tree folder which is less efficient
    def numTrees(self, n: int) -> int:
        # init. of dp arr. of size (n+1)
        dp = [0] * (n+1)

        # there are only 1 unique BST if there are 0/1 nodes
        dp[0] = 1
        dp[1] = 1

        # for each problem concerning up to k-nodes, we would always
        # be able to split into left/right subproblems that add up to k-1 nodes
        for i in range(2, n+1):
            for j in range(0, i-1+1):
                dp[i] += dp[j] * dp[i-1-j]
            
        return dp[n]
    
n = 3
n = 19

Solution().numTrees(n)