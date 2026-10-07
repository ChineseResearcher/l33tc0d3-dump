# dp - hard
from functools import cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) top-down DP with states (i, j, k), indicating we are solving
        # subproblem s[i:], with the curr. head of disjoint substring starting at j,
        # with k more disjoint substrings to create
        # 2) pre-compute the min. moves to convert into palindrome for any range [l...r]

        C = [ [0] * n for _ in range(n) ]
        for i in range(n - 1):
            for j in range(i + 1, n):
                l, r = i, j
                while l < r:
                    if s[l] != s[r]:
                        C[i][j] += 1
                    l += 1
                    r -= 1

        @cache
        def f(i: int, j: int, k: int) -> int:

            if i == n:
                return C[j][n - 1] if k == 0 else float('inf')

            # remaining string cannot produce k more substrings
            if k > n - i:
                return float('inf')

            res = float('inf')
            # do not split at curr. index
            res = fmin(res, f(i + 1, j, k))
            # split: s[j...i] is split as another disjoint substring
            if i < n - 1 and k > 0:
                res = fmin(res, C[j][i] + f(i + 1, i + 1, k - 1))

            return res

        return f(0, 0, k - 1)

s, k = "abc", 1
s, k = "abc", 2
s, k = "aabbc", 3
s, k = "leetcode", 8

Solution().palindromePartition(s, k)