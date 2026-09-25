# counting - medium
from collections import Counter
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        n = len(citations)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) the possible range of citation counts is small (i.e. <= 1000)
        # so we can use O(k) search to determine the h-index for k <= 1000

        c, freqSum, ans = Counter(citations), 0, 0
        for k in range(max(c.keys()) + 1):
            freq = c[k]
            if n - freqSum >= k:
                ans = fmax(ans, k)
            freqSum += freq

        return ans

citations = [100]
citations = [1,3,1]
citations = [3,0,6,1,5]

Solution().hIndex(citations)