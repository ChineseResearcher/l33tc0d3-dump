# counting - medium
from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:  

        n = len(s)

        ans = 0
        for i in range(n):

            # create a rolling hashtable to count char. freq
            rh = defaultdict(int)
            rh[s[i]] = 1

            for j in range(i+1, n):
                rh[s[j]] += 1

                # calculate beauty for this subarr.
                ans += max(rh.values()) - min(rh.values())

        return ans
    
s = "aabcb"
s = "aabcbaa"

Solution().beautySum(s)