# greedy - hard
from collections import Counter
from string import ascii_lowercase as L
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)
        # key ideas:
        # 1) first rule out "s" that cannot form a palindrome, i.e. having odd
        # count of a distinct char. more than once
        # 2) suppose m = n // 2, where n = len(s), we use enumeration + greedy
        # matching to test if we can form a palindromic permutation that is strictly greater
        # 3) we enumerate target[:i] for i <= m, s.t. target[i] is the 1st char.
        # to be lexicographically larger, and target[:i] is used as prefix of the palindrome
        c = Counter(s)

        odd_char = ''
        for char, freq in c.items():
            if freq % 2 == 1:
                if odd_char: return '' # no palindrome
                odd_char = char

        # fix the mid char. if any, we only care about the left / right partition
        if odd_char:
            c[odd_char] -= 1

        m = n // 2
        ans, i = '', 0
        while i < m:
            o = ord(target[i]) - ord('a')
            o += 1 # search for next larger char.
            while o < 26:
                # found a match
                char = L[o]
                if c[char] >= 2:
                    cc = c.copy()
                    cc[char] -= 2
                    # we make remainder in range [i+1...m] the smallest possible
                    rem = ''.join([x * (cc[x] // 2) for x in sorted(cc.keys())])
                    first_half = target[:i] + char + rem
                    # update answer       
                    ans = first_half + odd_char + first_half[::-1]
                    break
                o += 1

            # increment prefix
            if c[target[i]] - 2 < 0: break
            c[target[i]] -= 2
            i += 1

        # special case: the having target[:m] as the palindromic prefix,
        # the final palindrome is larger than target 
        if i == m:
            special_str = target[:m] + odd_char + target[:m][::-1]
            if special_str > target:
                return special_str

        return ans

s, target = "bb", "ba"
s, target = "aac", "abb"
s, target = "abc", "abb"
s, target = "baba", "bbaa"
s, target = "baba", "abba"

Solution().lexPalindromicPermutation(s, target)