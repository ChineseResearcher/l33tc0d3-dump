# greedy - medium
from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)

        ans = 0
        for i in range(k):
            ans += max(happiness[i]-i, 0)

        return ans
    
happiness, k = [1,2,3], 2
happiness, k = [1,1,1,1], 2
happiness, k = [2,3,4,5], 1

Solution().maximumHappinessSum(happiness, k)