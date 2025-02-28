# dp - hard
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # the editorial's answer treats dp table storing the Shortest
        # Common Superseq. (SCS) for diff. subproblems and backtrack from dp[-1][-1]

        # I find it much easier to approach from the perspective of LCS
        # because SCS = str1_apart_from_LCS + str2_apart_from_LCS + LCS

        # initiate a 2-D dp storing the Longest Common Subsequence (LCS) to
        # the subproblem conerning str1[i:] and str2[:j]
        dp = [ [''] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):

                # either LCS increments by 1 due to matched element
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]

                # or we only inherit from the option that produces longer LCS
                else:
                    if len(dp[i-1][j]) >= len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]

                    else:
                        dp[i][j] = dp[i][j-1]

        LCS = dp[m][n]
        # edge case: if LCS is empty string just return concatenation of s1 & s2
        if not LCS: return str1 + str2

        # for our LCS string at dp[m][n], we can reconstruct back our SCS
        # by using two pointers for str1 & str2 respectively
        s1_idx, s2_idx = 0, 0
        matchedIdx, ans = 0, []
        while True:

            # whenever the element at s1/s2 index is not equivalent to 
            # the LCS[idx] being matched, just append chars from s1/s2
            while s1_idx < m and str1[s1_idx] != LCS[matchedIdx]:
                ans.append(str1[s1_idx])
                s1_idx += 1

            while s2_idx < n and str2[s2_idx] != LCS[matchedIdx]:
                ans.append(str2[s2_idx])
                s2_idx += 1

            # otherwise, both s1/s2 indices now point to LCS[idx]
            ans.append(LCS[matchedIdx])
            # increment all indices
            matchedIdx += 1
            s1_idx += 1
            s2_idx += 1

            # exit the while-loop when all LCS chars have been loaded
            if matchedIdx == len(LCS):
                break

        # there can be unappended s1/s2 chars, collect them
        for i in range(s1_idx, m):
            ans.append(str1[i])
        for j in range(s2_idx, n):
            ans.append(str2[j])

        return ''.join(ans)

str1, str2 = "abac", "cab"
str1, str2 = "abb", "baa"
str1, str2 = "babba", "dbaad"
str1, str2 = "a", "bc"
str1, str2 = "ab", "abc"
str1, str2 = "bbbaaaba", "bbababbb"
str1 ,str2 = "bcacaaab", "bbabaccc"
str1 ,str2 = "aabbabaa", "aabbbbbbaa"

Solution().shortestCommonSupersequence(str1, str2)