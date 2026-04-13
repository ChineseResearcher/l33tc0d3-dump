# dp - hard
from collections import defaultdict
class Solution:
    def distinctSubseqII(self, s: str) -> int:

        n = len(s)
        # key ideas:
        # 1) think of linear dp where dp[i] represents the number of 
        # distinct subsequences up to s[i] and using s[i] as the last char.
        # 2) track the prefix sum of dp at each occurrence of character
        # in a hashmap: {'a':[pf1, pf2, ....]}

        dp = [0] * n

        pref_dp = defaultdict(list)

        MOD, dp_sum, ans = int(1e9+7), 0, 0
        for i in range(n):
            
            char = s[i]
            pref_dp[char].append(dp_sum)
            # unseen character
            if len(pref_dp[char]) == 1:
                dp[i] = dp_sum + 1 # add 1 as s[i] is also a subseq.
            else:
                dp[i] = dp_sum
                if len(pref_dp[char]) >= 2:
                    # de-duplicating
                    dp[i] -= pref_dp[char][-2]

            dp_sum += dp[i]
            ans += dp[i]
            ans %= MOD

        return ans

s = "abc"
s = "aba"
s = "aaa"
s = "abaca"

Solution().distinctSubseqII(s)