# bit manipulation - medium
from typing import List
from collections import Counter
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # this question can be easily done via brute-force
        # but the bit manipulation approach is elegant and worth taking note of

        # core idea:
        # 1) bitwise OR only stays the same / increases
        # 2) by tracking a hashmap for freq. of bitwise OR results, we could thus
        # use a deterministic for-loop to determine the count of max. bitwise OR
        # note: max. bitwise OR is equal to a[0] OR a[1] OR ... a[a.length - 1]
        prevBits = Counter([0])

        for num in nums:
            for prevBit, cnt in list(prevBits.items()):
                prevBits[prevBit | num] += cnt

        maxOR = 0
        for num in nums:
            maxOR |= num

        return prevBits[maxOR]
    
nums = [3,2,1,5]
nums = [2,2,2]
nums = [3,1]

Solution().countMaxOrSubsets(nums)