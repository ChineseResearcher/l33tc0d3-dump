# counting - medium
from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        # note that there are only 26 alphabets
        freq = [[char, f] for char, f in sorted(Counter(word).items(), key = lambda x: x[1])]

        # we have two possible strategies
        # 1) remove any characters with freq > min_freq + k
        # 2) remove any characters s.t. max_freq - min_freq <= k
        n = len(freq)

        ans, cnt1 = float('inf'), 0
        for i in range(n):

            min_freq, cnt2 = freq[i][1], 0
            for j in range(n-1, i, -1):

                if freq[j][1] > min_freq + k:
                    cnt2 += freq[j][1] - (min_freq + k)
                else:
                    break

            ans = min(ans, cnt1 + cnt2)
            # assume we removed all occurrences of curr. char
            cnt1 += min_freq

        return ans
    
word, k = "aabcaba", 0
word, k = "dabdcbdcdcd", 2
word, k = "aaabaaa", 2

Solution().minimumDeletions(word, k)