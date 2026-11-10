# dp - medium
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) linear DP with lookback up to 3 steps
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            for i in range(j - 1, j - 4, -1):
                if i < 0: break
                dp[j] = fmin(dp[j], dp[i] + costs[j - 1] + pow(j - i, 2))

        return dp[n]

n, costs = 3, [9.8,3]
n, costs = 4, [5,1,6,2]
n, costs = 4, [1,2,3,4]

Solution().climbStairs(n, costs)