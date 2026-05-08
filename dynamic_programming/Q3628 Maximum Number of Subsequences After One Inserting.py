# dp - medium
class Solution:
    def numOfSubsequences(self, s: str) -> int:

        # key ideas:
        # 1) as we only care about "LCT" subsequences, process the string
        # and update s to only contain "L", "C", "T"
        # 2) we need to think greedily where it is the best to place an
        # additional "L", "C" or "T"

        ss = []
        for c in s:
            if c in ["L", "C", "T"]:
                ss.append(c)

        s = ''.join(ss)

        # we design a helper to solve the dp problem of max. "LCT" subsequence cnt
        def f(s: str) -> int:

            n = len(s)
            # the design of the dp table is s.t.
            # 1) dp[0][i] is the prefix count of "L" up to i
            # 2) dp[1][i] is the subsequence count of "LC" up to i
            # 3) dp[2][i] is the subsequence count of "LCT" up to i
            dp = [ [0] * n for _ in range(3) ]

            if s[0] == 'L':
                dp[0][0] += 1

            for i in range(1, n):
                if s[i] == 'L':
                    dp[0][i] = dp[0][i-1] + 1
                    dp[1][i] = dp[1][i-1]
                    dp[2][i] = dp[2][i-1]
                elif s[i] == 'C':
                    dp[0][i] = dp[0][i-1]
                    dp[1][i] = dp[1][i-1] + dp[0][i-1]
                    dp[2][i] = dp[2][i-1]
                elif s[i] == 'T':
                    dp[0][i] = dp[0][i-1]
                    dp[1][i] = dp[1][i-1]
                    dp[2][i] = dp[2][i-1] + dp[1][i-1]

            return dp

        # case 1: additional L -> best at the front
        aL = f('L' + s)[2][-1]

        # case 2: additional T -> best at the back
        aT = f(s + 'T')[2][-1]

        # case 3: additional C -> best where combined count
        # of 'L' to the left and 'T' to the right is max.
        L_cnt, T_cnt = s.count('L'), 0

        best_cnt, best_i = 0, -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'L':
                L_cnt -= 1
            elif s[i] == 'T':
                T_cnt += 1

            if L_cnt + T_cnt > best_cnt:
                best_cnt = L_cnt + T_cnt
                best_i  = i

        aC = f(s[:best_i] + 'C' + s[best_i:])[2][-1]

        return max(aL, max(aT, aC))
    
s = "L"
s = "LMCT"
s = "LCCT"
s = "LCTKLCLT"
s = "LCLPTTGC"
s = "LLLTCTCT"

Solution().numOfSubsequences(s)