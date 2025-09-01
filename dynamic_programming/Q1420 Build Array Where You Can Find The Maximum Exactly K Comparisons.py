# dp - hard
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        N, M, K = n, m, k
        # dp[n][k][m] represents solution to a length-n array 
        # with search costs = k and that the maximum number appeared is m
        dp = [ [ [0] * (M+1) for _ in range(K+1) ] for _ in range(N+1) ]
        for m in range(1, M+1):
            dp[1][1][m] = 1

        MOD = int(1e9 + 7)
        for n in range(2, N+1):
            for k in range(1, K+1):

                # pfSum of dp[n-1][k-1]
                pfs, cSum = [], 0
                for x in dp[n-1][k-1]:
                    cSum += x
                    pfs.append(cSum)

                for m in range(1, M+1):
                    # op1: adding this number would bring a new maximum "m"
                    # thus inherit from dp[n-1][k-1][1,2,...,m-1]
                    dp[n][k][m] += pfs[m-1]

                    # op2: adding this number would not change the maximum
                    # and search costs remain the same, and we would inherit from
                    # dp[n-1][k][m] where (k, m) stays unchanged
                    dp[n][k][m] += m * dp[n-1][k][m]

                    dp[n][k][m] %= MOD

        return sum(dp[N][K]) % MOD
    
n, m, k = 2, 3, 1
n, m, k = 5, 2, 3
n, m, k = 9, 1, 1
n, m, k = 50, 100, 50 # constraint

Solution().numOfArrays(n, m, k)