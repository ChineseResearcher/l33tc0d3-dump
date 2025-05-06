# sliding window - medium
from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:    

        n = len(s)
        # notice that for some window sizes a & b, if a < b
        # then the occurrences of window size of a must be >= that of b
        # then we can avoid checking every window size up to maxSize, and only check the minSize
        ws = minSize
        substr_freq = defaultdict(int)
        
        l, window = 0, dict()
        for r in range(ws):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
        
        if len(window) <= maxLetters:
            substr_freq[s[:ws]] += 1
        
        # continue sliding fixed window
        for r in range(ws, n):
            
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            
            l += 1
                
            if len(window) <= maxLetters:
                substr_freq[s[l:r+1]] += 1

        return max(substr_freq.values()) if substr_freq else 0
    
s, maxLetters, minSize, maxSize = "aababcaab", 2, 3, 4
s, maxLetters, minSize, maxSize = "aaaa", 1, 3, 3
s, maxLetters, minSize, maxSize = "abcde", 2, 3, 3

Solution().maxFreq(s, maxLetters, minSize, maxSize)