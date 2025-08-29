# dp - hard
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [ [0] * (k+1) for _ in range(n+1) ]
        dp[0][0] = 1

        MOD = int(1e9 + 7)
        for i in range(1, n+1):

            # prefix sum of dp[i-1]
            pfSum, cSum = [], 0
            for j in range(k+1):
                cSum += dp[i-1][j]
                pfSum.append(cSum)

            for j in range(k+1):
                # inherit from (i-1, j), (i-1, j-1), ..., (i-1, j-i+1)
                if j - i >= 0:
                    dp[i][j] += pfSum[j] - pfSum[j-i]
                else:
                    dp[i][j] += pfSum[j]

            dp[i][j] %= MOD
            
        return dp[n][k]
    
n, k = 3, 0
n, k = 3, 1
n, k = 1000, 1000

Solution().kInversePairs(n, k)