# dp - hard
import numpy as np
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        MOD = int(1e9+7)
        # key ideas:
        # 1) construct dp[0...r][0/1] where dp[i][0] denotes the count
        # of zigzag arrays ending at i, and index i is the localMin,
        # conversely for dp[i][1] where it indicates the localMax
        # 2) apply prefix sum for dp accounting, use rolling dp to save space
        # 3) O(n*r) is supposed to pass? But too slow, so optimized w/ numpy

        dp = np.zeros((r + 1, 2), dtype=np.int64)

        # initialization
        dp[l:r+1, :] = 1

        for _ in range(n - 1):
            new_dp = np.zeros_like(dp)

            # localMin (state 0)
            # the array version:
            # for j in range(r-1, l-1, -1):
            #     new_dp[j][0] += (new_dp[j+1][0] + dp[j+1][1]) % MOD
            new_dp[l:r, 0] = np.cumsum(dp[l+1:r+1, 1][::-1])[::-1] % MOD

            # localMax (state 1)
            # the array version:
            # for i in range(l+1, r+1):
            #     new_dp[i][1] = (new_dp[i-1][1] + dp[i-1][0]) % MOD
            new_dp[l+1:r+1, 1] = np.cumsum(dp[l:r, 0]) % MOD

            dp = new_dp

        return int(dp.sum() % MOD)

n, l, r = 3, 4, 5
n, l, r = 3, 1, 3
n, l, r = 2000, 1, 2000 # constraint

Solution().zigZagArrays(n, l, r)