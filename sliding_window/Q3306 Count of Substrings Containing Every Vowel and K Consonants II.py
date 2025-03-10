# sliding window - medium
from collections import deque
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        n = len(word)
        # 26 alphabets = 5 vowels ('a','e','i','o','u') + 21 consonants
        vowelCnt = {'a':-1, 'e':-1, 'i':-1, 'o':-1, 'u':-1}

        # init consonantCnt
        csnCnt, csnPos = 0, deque([])

        ans, l = 0, 0
        for r in range(n):

            # mark the latest idx that a vowel appears
            if word[r] in vowelCnt:
                vowelCnt[word[r]] = r
            else:
                csnCnt += 1
                csnPos.append(r)

            # excess csnCnt triggers shrinking left pointer
            while csnCnt > k:
                if word[l] not in vowelCnt:
                    csnCnt -= 1
                    csnPos.popleft()

                l += 1

            # validate a desired substring
            if all(idx >= l for idx in vowelCnt.values()) and csnCnt == k:
                if k > 0:
                    ans += min(min(vowelCnt.values()), csnPos[0]) - l + 1
                else:
                    ans += min(vowelCnt.values()) - l + 1

        return ans
    
word, k = "ieaouqqieaouqq", 1
word, k = "aeioqq", 1
word, k = "aeiou", 0
word, k = "iqeaouqi", 2
word, k = "aoaiuefi", 1
word, k = "aeeieoua", 0

Solution().countOfSubstrings(word, k)