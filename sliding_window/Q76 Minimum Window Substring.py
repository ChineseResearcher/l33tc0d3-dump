# sliding window - hard
from collections import Counter
class Solution:
    def checkIfContain(self, window, ref):
        for k in ref.keys():
            if window[k] < ref[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
    
        # build a reference frequncy map from t
        ref = Counter(t)

        # maintain a window dict
        window = {k:0 for k in ref.keys()}

        minLength = float('inf')
        min_l, min_r = -1, -1

        l = 0
        for r, char in enumerate(s):

            # only characters that are included in t should trigger window operations
            if char in ref:

                window[char] += 1
                if self.checkIfContain(window, ref):

                    # shrink the left pointer if possible
                    while True:
                        if s[l] in ref and window[s[l]] - 1 < ref[s[l]]:
                            break
                        
                        if s[l] in ref: window[s[l]] -= 1
                        l += 1
                    
                    # compute curr length
                    if r-l+1 < minLength:
                        min_l, min_r = l, r
                        minLength = r-l+1
                    
        return s[min_l:min_r+1]
    
s, t = "ADOBECODEBANC", "ABC"
s, t = "a", "a"
s, t = "a", "aa"

Solution().minWindow(s, t)