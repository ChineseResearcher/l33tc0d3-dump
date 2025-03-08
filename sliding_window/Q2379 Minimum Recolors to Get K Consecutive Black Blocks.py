# sliding window - easy
from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)

        # we just need to monitor for a fixed size sliding window of size k
        # what is the mininum number of 'W' chars present
        # Note: we are guranteed that n >= k
        windowFreq = Counter(blocks[:k])
        
        # init. the ans to 'W' count
        ans = windowFreq['W']
        for i in range(k, n):
            windowFreq[blocks[i]] += 1
            windowFreq[blocks[i-k]] -= 1

            ans = min(ans, windowFreq['W'])

        return ans