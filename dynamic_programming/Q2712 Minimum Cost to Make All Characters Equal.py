# dp - medium
class Solution:
    def minimumCost(self, s: str) -> int:

        n = len(s)
        # core ideas:
        # for an index i, if we want to find out the costs for s[0...i] to be all 0s
        # we have two options (if s[i] == 0):
        # 1) assume s[0...i-1] have all been converted to 0s, and simply take dp[i-1][0]
        # 2) assume s[0...i-1] have all been converted to 1s and take dp[i-1][1] + a conversion cost
        # of (i-1+1) to have s[0...i-1] to be all converted to 0s
        # and then same derivation happens for other scenarios

        def dp_helper(s):

            dp = [[None] * 2 for _ in range(n)]
            if s[0] == '0':
                dp[0][0], dp[0][1] = 0, 1
            elif s[0] == '1':
                dp[0][0], dp[0][1] = 1, 0

            for i in range(1, n):

                if s[i] == '0':
                    dp[i][0] = min(dp[i-1][0], dp[i-1][1] + i)
                    dp[i][1] = min(dp[i-1][0] + i + 1, dp[i-1][1] + 2*i + 1)

                elif s[i] == '1':
                    dp[i][0] = min(dp[i-1][0] + 2*i + 1, dp[i-1][1] + i + 1)
                    dp[i][1] = min(dp[i-1][0] + i, dp[i-1][1])

            return dp

        dp1, dp2 = dp_helper(s), dp_helper(s[::-1])

        ans = min(min(dp1[-1]), min(dp2[-1]))
        for i in range(n-1):
            ans = min(ans, dp1[i][0] + dp2[n-2-i][0])
            ans = min(ans, dp1[i][1] + dp2[n-2-i][1])

        return ans
    
s = "0011"
s = "010101"

Solution().minimumCost(s)