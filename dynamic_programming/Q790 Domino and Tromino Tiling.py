# dp - medium
class Solution:
    def numTilings(self, n: int) -> int:
        # this question is a pure math induction problem
        # since it is extremely difficult to draw for n = 4 already
        # it is easier to develop the pattern by getting WAs from the judge

        if n <= 2:
            return 1 if n == 1 else 2

        dp = [0] * (n+1)
        # n = 1 only has 1 way of arranging
        # while n = 2 only has two ways of arranging
        dp[1], dp[2] = 1, 2
        # to facilitate the transition pattern below
        # dp[0] has to be 1
        dp[0] = 1 

        MOD = int(1e9 + 7)
        for i in range(3, n+1):
            dp[i] = (dp[i-1]*2 + dp[i-3]) % MOD

        return dp[-1]
    
n = 1 # only one way of placing a vertical domino
n = 3
n = 5
n = 7
n = 1000

Solution().numTilings(n)