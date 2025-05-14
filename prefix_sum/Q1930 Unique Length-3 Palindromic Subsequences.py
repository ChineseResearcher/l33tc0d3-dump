# prefix sum - medium
from string import ascii_lowercase as asc
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s)

        # initiate a prefix sum arr storing snapshot freq. dict of alphabets
        pf_sum = [None] * n
        # snapshot dict stores the frequency of 26 alphabets at any index i
        snapshot = {i:0 for i in asc}

        for idx, char in enumerate(s):
            snapshot[char] += 1
            pf_sum[idx] = snapshot.copy()

        ans = set()
        # notice that length-3 palindrome only has 1 alphabet in the middle
        # which means we only need to iterate from 1 to n-1 
        for i in range(1, n-1):

            # constant time as number of alphabets is fixed
            # get the frequency of alphabets before and after index i
            prev = pf_sum[i-1]
            next = {char: (pf_sum[-1][char] - pf_sum[i][char]) for char in asc}

            for char in asc:
                if prev[char] > 0 and next[char] > 0:
                    ans.add(char + s[i] + char)

        return len(ans)

s = "adc"
s = "aabca"
s = "bbcbaba"
s = "ckafnafqo"

Solution().countPalindromicSubsequence(s)
