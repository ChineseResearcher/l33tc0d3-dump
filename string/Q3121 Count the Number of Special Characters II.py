# string - medium
import string
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        w = dict()
        for i, c in enumerate(word):
            if c not in w:
                w[c] = i
            # update last occurrence index of lowercase letter
            if c == c.lower():
                w[c] = i

        ans = 0
        for c in string.ascii_lowercase:
            if c in w and c.upper() in w and w[c] < w[c.upper()]:
                ans += 1

        return ans

word = "abc"
word = "AbBCab"
word = "aaAbcBC"

Solution().numberOfSpecialChars(word)