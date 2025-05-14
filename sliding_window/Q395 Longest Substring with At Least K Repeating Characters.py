# sliding window - medium
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        # this is an unconventional sliding window problem, we can't
        # possibly extract the longest substring with all chars repeated >= k times
        # in just one go, instead we need to experiment with a range of 
        # number of unique characters to include in the window
        # e.g. elementCnt = 2, we would only have windows like [a,a,b,b,a], [b,c,b], [d,e,e,d]
        # shrink the left end whenever number of elements exceed 2 in the window

        # upper bound is set to the number of unique chars
        ans = 0
        for elementCnt in range(1, len(set(s))+1):

            l, window = 0, dict()
            for r in range(n):

                if s[r] not in window:
                    window[s[r]] = 0
                window[s[r]] += 1

                # control number of elements
                while len(window) > elementCnt:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]

                    l += 1

                isValid = True
                for v in window.values():
                    if v < k:
                        isValid = False
                        break

                if isValid:
                    ans = max(ans, r-l+1)
                    
        return ans
    
s, k = "aaabb", 3
s, k = "ababbc", 2
s, k = "ababacb", 3
s, k = "bbaaacddcaabdbd", 3

Solution().longestSubstring(s, k)