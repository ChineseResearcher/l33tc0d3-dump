# dp - medium
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        dp = [0] * len(s)

        one_cnt = 0
        for idx, char in enumerate(s):

            # counting of seen 1s
            one_cnt += 1 if char == '1' else 0

            # when s[idx] = 1, 
            # we always inherit the prev dp val, e.g. '00101' 
            # first violation occurs at index 3, we could either rectified to '00(0)11' or '001(1)1'
            # and thus when we are at index 4, we inherit dp[3] = 1
            if char == '1':
                dp[idx] = dp[idx-1]

            # when s[idx] = 0, transition logic depends on whether
            # it is more costly to invert all RELEVANT 0s to 1s OR all 1s to 0s
            # e.g. 011(0011010001), invalid part is bracketed
            # 0s to 1s: 6 flips
            # 1s to 0s: 5 flips
            # then answer is the minimum of the two options
            else:
                dp[idx] = min(dp[idx-1] + 1, one_cnt)

        return dp[-1]
    
s = "11011"
s = "010110"
s = "01000101"
s = "0101100011"
s = "10011111110010111011"
s = "0110011010001010011100011"

Solution().minFlipsMonoIncr(s)