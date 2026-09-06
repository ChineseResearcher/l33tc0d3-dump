# dp - hard
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        # key ideas:
        # 1) knapsack DP on string matching

        @cache
        def f(sIdx:int, tIdx:int) -> int:

            # t fully matched
            if tIdx == n: return 1

            # exhausted all characters of s
            if sIdx == m: return 0

            # op1: leave it
            currAns = f(sIdx + 1, tIdx)

            # op2: match it
            if s[sIdx] == t[tIdx]:
                currAns += f(sIdx + 1, tIdx + 1)

            return currAns
            
        return f(0, 0)

s, t = "aabb", "ab"
s, t = "babgbag", "bag"
s, t = "rabbbit", "rabbit"

Solution().numDistinct(s, t)