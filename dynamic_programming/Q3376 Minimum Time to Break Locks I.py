# dp - medium
from typing import List
from functools import cache
class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        
        n = len(strength)
        # core ideas:
        # 1) encode three states: (unlocked, energy, x)
        # 2) unlocked is a bitmask where set bit would 
        # indicate that the i-th lock has been broken
        # 3) backtrack + caching for speed boost

        @cache
        def backtrack(unlocked, energy, x):

            if unlocked == (2 << (n-1)) - 1:
                return 0
            
            curr_res = float('inf')
            # exploring locks that can be broken
            for bit in range(n):
                # detect an unbroken lock
                if unlocked & (1 << bit) == 0:
                    
                    # can break
                    if energy >= strength[bit]:

                        # unlock
                        unlocked |= (1 << bit)
                        curr_res = min(curr_res, 
                                    1 + backtrack(unlocked, x+k, x+k))
                        
                        # roll back unlock
                        unlocked &= ~(1 << bit)

                    # must wait first
                    else:
                        e_diff = strength[bit] - energy

                        if e_diff % x == 0:
                            t_inc, e_new = e_diff // x, strength[bit]
                        else:
                            t_inc = (e_diff // x) + 1
                            e_new = energy + t_inc * x 

                        curr_res = min(curr_res, t_inc + backtrack(unlocked, e_new, x))

            return curr_res

        return backtrack(0, 0, 1) - 1
    
strength, k = [3,4,1], 1
strength, k = [2,5,4], 2
strength, k = [461515], 5
strength, k = [7,3,6,18,22,50], 4
strength, k = [112233, 998877, 335588, 678951, 458761, 123411, 432111, 999911], 10 # constraint

Solution().findMinimumTime(strength, k)