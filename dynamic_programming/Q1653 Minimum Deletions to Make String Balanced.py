# dp - medium
class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) same as Q926 Flip String to Monotone Increasing
        # 2) need an additional count tracker to achieve O(n) DP
        b_cnt = 0

        dp = [0] * n
        for i, char in enumerate(s):

            if char == 'a':
                del_a = dp[i-1] + 1
                del_b = b_cnt

                dp[i] = fmin(del_a, del_b)

            else:
                b_cnt += 1
                if i > 0: dp[i] = dp[i-1]

        return dp[-1]
    
s = "aaa"
s = "aababbab"
s = "bbaaaaabb"

Solution().minimumDeletions(s)