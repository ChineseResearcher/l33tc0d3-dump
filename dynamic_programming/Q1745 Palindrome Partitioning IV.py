# dp - hard
from functools import cache
class Solution:
    def checkPartitioning(self, s: str) -> bool:

        n = len(s)
        # key ideas:
        # 1) first pre-compute the palindromes for every range using bottom-up DP
        # 2) solve top-down DP with states (i, k), and check validity of each split
        # using result from (1)

        dp = [ [False] * n for _ in range(n) ]

        # check palindromes of length 1/2
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # check palindromes of length > 2
        for l in range(2, n):
            for i in range(n - l):
                if s[i] == s[i + l] and dp[i + 1][i + l - 1]:
                    dp[i][i + l] = True

        @cache
        def f(i: int, k: int) -> bool:

            if k == 0:
                if i < n:
                    return dp[i][n - 1]
                else:
                    return False

            # for every valid split, try a cut here
            for j in range(i, n):
                if dp[i][j] and f(j + 1, k - 1):
                    return True

            return False

        # 2 more splits to create exactly 3 substrings
        return f(0, 2) 

s = "abcbdd"
s = "bcbddxy"

Solution().checkPartitioning(s)