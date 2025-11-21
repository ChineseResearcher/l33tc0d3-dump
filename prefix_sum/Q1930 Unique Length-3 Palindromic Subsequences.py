# prefix sum - medium

# prefix / suffix processing + bitmask solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s)
        # build two bitmasks: prefix and suffix
        # purpose: keep track of appeared letters up to a certain index
        pf_mask, curr_mask = [], 0
        for i in range(n):

            char_ord = ord(s[i]) - ord('a')
            curr_mask |= (1 << char_ord)

            pf_mask.append(curr_mask)

        sf_mask, curr_mask = [], 0
        for i in range(n-1, -1, -1):

            char_ord = ord(s[i]) - ord('a')
            curr_mask |= (1 << char_ord)

            sf_mask.append(curr_mask)

        sf_mask = sf_mask[::-1]

        unique = [ [0] * 26 for _ in range(26) ] # storing "aba" as "1" -> "0"
        # explore indices in range [1...n-2] to identify unique palindrome
        for i in range(1, n-1):

            common = pf_mask[i-1] & sf_mask[i+1]
            if common == 0:
                continue

            if s[i] == s[i-1]:
                if i-2 >= 0 and s[i-1] == s[i-2]:
                    continue

            char_ord = ord(s[i]) - ord('a')
            
            m = common.bit_length()
            for j in range(m):
                if common & (1 << j) != 0:
                    unique[char_ord][j] = 1

        ans = 0
        for x in unique:
            ans += sum(x)

        return ans

# two-pointer solution (much faster)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s) 
        # key ideas:
        # 1) length-3 palindrome must be in the form of a_a
        # 2) for every unique character in s, find the leftmost / rightmost 
        # occurrence index, and if they are indeed apart, it would be forming
        # valid palindromes with any unique characters in between

        if n <= 2:
            return 0

        charSet = set(s)
        
        ans = 0
        for ch in charSet:
            l = s.find(ch)
            r = s.rfind(ch)

            if l != r:
                ans += len(set(s[l + 1:r]))

        return ans

s = "adc"
s = "aabca"
s = "bbcbaba"
s = "ckafnafqo"

Solution().countPalindromicSubsequence(s)
