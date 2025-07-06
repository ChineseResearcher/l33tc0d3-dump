# dp - medium
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        # construct dp of size n
        dp = [0] * n

        # init. a array-based dict of length 26 to
        # store the last desired index of a character
        char_pos = [-1] * 26

        ans = 0
        for i in range(n):

            curr = word[i]
            # need to always inherit from previous because
            # dp[i] represents the answer if we consider up to word[:i]
            # note: this is unlike LIS-dp where dp[i] represents the answer
            # if arr[i] is used as the end of LIS
            dp[i] = dp[i-1]

            arr_idx = ord(curr) - ord('a')
            if char_pos[arr_idx] == -1:
                char_pos[arr_idx] = i
                continue

            if i - char_pos[arr_idx] >= 3:
                dp[i] = max(dp[i], dp[char_pos[arr_idx]] + 1)
                char_pos = [-1] * 26

            ans = max(ans, dp[i])

        return ans
    
word = "abcdeafdef"
word = "abeaebddae"
word = "accbabdeb"

Solution().maxSubstrings(word)