# dp - medium
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        # key ideas:
        # 1) the natural recurrence follows:
        # if s[i] != t[j], then we conclude the count of diff-by-one substrings
        # ending at (i, j) as count of exact-match substrings ending at (i-1, j-1) + 1
        # 2) compute the dp table for exact-match, followed by diff-by-one

        dp_exact = [ [0] * n for _ in range(m) ]
        # init. for first char. of "s" & "t": set 1 if matched
        for j in range(n):
            if s[0] == t[j]: dp_exact[0][j] = 1
        for i in range(1, m):
            if s[i] == t[0]: dp_exact[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if s[i] == t[j]:
                    dp_exact[i][j] = dp_exact[i-1][j-1] + 1

        dp_diff_one, ans = [ [0] * n for _ in range(m) ], 0
        # init. for first char. of "s" & "t": set 1 if NOT matched
        for j in range(n):
            if s[0] != t[j]:
                dp_diff_one[0][j] = 1
                ans += 1
        for i in range(1, m):
            if s[i] != t[0]:
                dp_diff_one[i][0] = 1
                ans += 1

        for i in range(1, m):
            for j in range(1, n):
                if s[i] != t[j]:
                    dp_diff_one[i][j] = dp_exact[i-1][j-1] + 1
                else:
                    dp_diff_one[i][j] = dp_diff_one[i-1][j-1]

                # accounting for every possible ending
                ans += dp_diff_one[i][j]

        return ans

s, t = 'ab', 'aa'
s, t = 'aba', 'baba'
s, t = "bbabbbbaab", "aaabbbbbbb"

Solution().countSubstrings(s,t)