# bit manipulation - medium
from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        powers = []
        for pos in range(32):
            if n & (1 << pos) != 0:
                powers.append(1 << pos)

        # build a prefix sum for sum product
        pf_sum, curr_prod = [], 1
        for x in powers:
            curr_prod *= x
            # curr_prod %= MOD
            pf_sum.append(curr_prod)

        ans, MOD = [], int(1e9 + 7)
        for l, r in queries:
            ans.append((pf_sum[r] // (pf_sum[l-1] if l > 0 else 1)) % MOD)

        return ans
    
n, queries = 15, [[0,1],[2,2],[0,3]]
n, queries = 2, [[0,0]]

Solution().productQueries(n, queries)