# dp - hard
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n, m = len(strs), len(strs[0])
        # key ideas:
        # 1) invert the problem to find the common LIS for all strings
        # 2) O(n^3) loop with O(n^2) allocated to DP states scanning
        dp = [1] * m

        fmax = lambda a, b: a if a >= b else b

        LIS = 1
        for i in range(1, m):
            for j in range(i):

                # check across all strs to determine if strs[k][i] 
                # >= strs[k][j] for all k in range [0, n]
                valid = True
                for k in range(n):
                    if strs[k][i] < strs[k][j]:
                        valid = False
                        break

                if valid:
                    dp[i] = fmax(dp[i], dp[j] + 1)
                    LIS = fmax(LIS, dp[i])

        return m - LIS

strs = ["edcba"]
strs = ["baabab"]
strs = ["babca","bbazb"]
strs = ["ghi","def","abc"]

Solution().minDeletionSize(strs)