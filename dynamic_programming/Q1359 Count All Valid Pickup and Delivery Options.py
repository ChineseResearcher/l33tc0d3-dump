# dp - hard
class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        MOD = int(1e9 + 7)
        for i in range(2, n+1):

            # some knowledge of PnC applied:
            # if we want to know the answer to n = k
            # we look at combinations under n = k - 1
            # i.e. every combination would have length m = 2 * (k - 1)
            # then we would have (m+1 + m + (m-1) + ... + 1) ways to add a new valid pair
            # for each of the valid combinations, forming natural inheritance
            m = (i-1) * 2
            multiplier = (m + 1 + 1) * (m+1) // 2
            dp[i] = (dp[i-1] * multiplier) % MOD

        return dp[-1] 
    
n = 1
n = 2
n = 3
n = 500
n = int(1e5)

Solution().countOrders(n)