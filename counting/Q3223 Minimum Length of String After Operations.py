# counting - medium
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)

        n = len(s)
        ans = n
        # keep decrementing our ans until it becomes the min. length
        for alphabet, f in freq.items():

            # for odd-count, e.g. "aaa", we can at most reduce to "a"
            if f % 2 == 1:
                ans -= (f // 2) * 2
            # for even-count, e.g. "bbbb", we can at most reduce to "bb"
            else:
                ans -= (f // 2 - 1) * 2

        return ans
    
s = "abaacbcbb"

Solution().minimumLength(s)
