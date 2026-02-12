# counting - medium
from collections import Counter
class Solution:
    def longestBalanced(self, s: str) -> int:
        
        n = len(s)
        fmax = lambda a, b: a if a > b else b

        ans = 0
        for i in range(n):

            # early stop
            if n-i <= ans:
                break

            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                
                balanced_cnt, balanced = None, True
                for f in freq.values():
                    if balanced_cnt is None:
                        if f > 0:
                            balanced_cnt = f
                    else:
                        if f != balanced_cnt:
                            balanced = False
                            break

                if balanced:
                    ans = fmax(ans, j-i+1)

        return ans

s = "aba"
s = "abbac"
s = "zzabccy"

Solution().longestBalanced(s)