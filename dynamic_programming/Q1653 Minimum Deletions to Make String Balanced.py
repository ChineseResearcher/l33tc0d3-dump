# dp - medium
class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        # this problem is the exact same as Q926 Flip String to Monotone Increasing
        # where we would need an additional count tracker to achieve O(n) DP
        b_cnt = 0

        dp = [0] * n
        for i, char in enumerate(s):

            if char == 'a':
                # we only recognise the "invalid" As appearing after the first B
                del_a = dp[i-1] + 1 if b_cnt > 0 else 0
                del_b = b_cnt

                dp[i] = min(del_a, del_b)

            else:
                b_cnt += 1
                if i > 0:
                    dp[i] = dp[i-1]

        return dp[-1]
    
s = "aababbab"
s = "bbaaaaabb"
s = "aaa"

Solution().minimumDeletions(s)