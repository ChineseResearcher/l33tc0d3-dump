# prefix sum - medium
from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        ans = float('-inf')
        for startIdx in range(k):
            
            # first derive all indices that we can land on
            jump_idx = list(range(startIdx, len(energy), k))
            
            # then jump in reverse direction and keep track
            # of a suffix sum to represent the total gain by starting 
            # the jump at any of the indices
            cSum = 0
            for i in range(len(jump_idx)-1, -1, -1):
                cSum += energy[jump_idx[i]]
                
                if cSum > ans:
                    ans = cSum

        return ans
    
energy, k = [5,2,-10,-5,1], 3
energy, k = [-2,-3,-1], 2

Solution().maximumEnergy(energy, k)