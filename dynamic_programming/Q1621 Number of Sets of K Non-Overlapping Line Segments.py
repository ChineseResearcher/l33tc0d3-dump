# dp - medium
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        N, K = n, k + 1
        MOD = int(1e9 + 7)
        # key ideas:
        # 1) build table dp[k][n] where it indicates the solution to subproblem
        # concerning n points and exactly k segments
        # 2) transition from two prev. states:
        # - dp[k - 1][0...n - 1] (maintain a prefix sum)
        # - dp[k][n - 1] (skip curr.)
        dp = [ [0] * N for _ in range(K) ]

        # 1 way to place no segments
        for n in range(N):
            dp[0][n] = 1

        dp_r_pf = [0] * K
        dp_r_pf[0] = 1

        for n in range(1, N):
            for k in range(1, K):
                dp[k][n] += dp[k][n - 1]
                dp[k][n] += dp_r_pf[k - 1]
                dp[k][n] %= MOD
                
            for k in range(K):
                # update row prefix of our DP table
                dp_r_pf[k] += dp[k][n]
                dp_r_pf[k] %= MOD

        return dp[K - 1][N - 1]

n, k = 4, 2
n, k = 3, 1
n, k = 30, 7

Solution().numberOfSets(n, k)