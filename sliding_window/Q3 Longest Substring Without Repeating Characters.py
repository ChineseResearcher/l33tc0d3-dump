# sliding window - medium
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        # store the freq. of characters in the curr. sliding window
        window_freq = defaultdict(int)

        l, ans = 0, 0
        for r in range(n):

            curr = s[r]
            # increment curr's freq
            window_freq[curr] += 1

            # shrink left if necessary to ensure no
            # repeared character(s) in the window
            while window_freq[curr] > 1:

                window_freq[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans
    
s = "abcabcbb"
s = 'bbbbb'
s = 'pwwkew'
s = "dvdf"

Solution().lengthOfLongestSubstring(s)