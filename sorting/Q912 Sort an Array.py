# sorting - medium
from typing import List
from collections import Counter
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # key ideas:
        # 1) we can use counting sort as the range of values is not big
        # 2) iterate from min to max, and fill in the sorted values
        # according to pre-computed frequencies stored in a hashmap
        freq = Counter(nums)
        a, b = min(freq), max(freq)

        ans, i = [None] * n, 0
        for x in range(a, b+1):
            if freq[x]:
                for _ in range(freq[x]):
                    ans[i] = x
                    i += 1

        return ans
    
nums = [5,2,3,1]
nums = [5,1,1,2,0,0]

Solution().sortArray(nums)