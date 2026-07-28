# sorting - medium
from collections import Counter
from string import ascii_lowercase as lo
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        # key ideas:
        # 1) observe that an even-length palindrome must have every
        # char. count divisible by 2, whereas an odd-length has 1 char. w/ odd cnt
        # 2) in the case of odd-length palindrome, the char. w/ odd cnt
        # needs to be in the middle of the final palindrome
        freq = Counter(s)

        halve = []
        for c in lo:
            if freq[c] > 0:
                # assignment frequency
                t = freq[c] // 2
                halve.append(c * t)
                freq[c] -= t * 2

        mid = []
        # take care of odd-cnt char.
        for c in lo:
            if freq[c] > 0:
                mid.append(c)

        return ''.join(halve + mid + halve[::-1])

s = "z"
s = "babab"
s = "daccad"

Solution().smallestPalindrome(s)