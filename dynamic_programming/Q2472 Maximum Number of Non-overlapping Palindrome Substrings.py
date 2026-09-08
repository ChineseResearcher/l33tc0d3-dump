# dp - hard
from typing import List
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) solve longest palindromic substring problem, s.t. dp1[i][j] indicates
        # if s[i...j] is a palindromic substring
        # 2) iterate through "s", and for s[:i], find the shortest suffix that satisfies
        # being a palindromic substring, and perform dp accounting

        def lps(s:str) -> List[List[bool]]:

            dp = [ [False] * n for _ in range(n) ]

            for i in range(n - 1):
                dp[i][i] = True
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = True
            dp[n - 1][n - 1] = True

            for length in range(3, n + 1):
                for j in range(n - length + 1):
                    l = j
                    r = l + length - 1
                    if s[l] == s[r] and dp[l + 1][r - 1]:
                        dp[l][r] = True

            return dp

        dp1 = lps(s)

        # dp2[i] indicates the solution to the subproblem concerning s[:i]
        dp2 = [0] * n

        for i in range(n):
            if i > 0:
                dp2[i] = dp2[i - 1]

            # greedily look for the shortest suffix ending at i
            for j in range(i - k + 1, -1, -1):
                if dp1[j][i]:
                    dp2[i] = fmax(dp2[i], 1 + (dp2[j - 1] if j - 1 >= 0 else 0))
                    break
            
        return dp2[-1]

s, k = "adbcda", 2
s, k = "abaccdbbd", 3

Solution().maxPalindromes(s, k)