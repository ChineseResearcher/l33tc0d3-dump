# counting - medium
from typing import List
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        # to form the longest palindrome, for each words[i] w/ length = 2
        # we need to differentiate between the case of 'xx' & 'xy'
        freq = Counter(words)

        # maintain a set storing processed pairs
        seen = set()

        ans, wordLen, xx_odd = 0, 2, False
        for k, v in freq.items():

            if k not in seen:
                # case 1) 'xy'
                if k[0] != k[1]:
                    ans += 2 * min(v, freq[k[1] + k[0]]) * wordLen
                    seen.add(k)
                    seen.add(k[1] + k[0])

                # case 2) 'xx'
                else:
                    if v % 2 != 0:
                        xx_odd = True

                    ans += 2 * (v // 2) * wordLen
                    
        if xx_odd:
            ans += 2

        return ans
    
words = ["lc","cl","gg"]
words = ["cc","ll","xx"]
words = ["ab","ty","yt","lc","cl","ab"]
words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

Solution().longestPalindrome(words)