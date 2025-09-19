# dp - hard
from functools import cache
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        m, n = len(ring), len(key)

        @cache
        def recursive_play(ring_idx, key_idx):

            # complete typing
            if key_idx == n:
                return 0
            
            # explore the next-to-type char
            target = key[key_idx]

            res = float('inf')
            for i in range(ring_idx, ring_idx + m):
                # rectified ring_idx 
                ii = i % m

                if ring[ii] == target:
                    # compute clockwise & anticlockwise moves
                    acw = i - ring_idx
                    cw = m - acw

                    # add one for pressing button
                    optim_mv = min(acw, cw) + 1 
                    res = min(res, optim_mv + recursive_play(ii, key_idx + 1))

            return res

        return recursive_play(0, 0)
    
ring, key = "godding", "gd"
ring, key = "godding", "godding"
ring, key = "ababcab", "acbaacba"
ring, key = "abcd" * 25, "ab" * 50 # constraint

Solution().findRotateSteps(ring, key)