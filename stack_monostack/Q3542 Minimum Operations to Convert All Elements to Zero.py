# monotonic stack - medium
from typing import List
from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) use a monotonic stack to pre-compute the right smaller of all nums[i]
        # 2) iterate through nums and keep track of the rightmost imaginary bound defined
        # by the right smaller index of an unique number
        rb_covered = defaultdict(int)

        monoAsc, rightSmaller = [], [n] * n
        for i in range(n):

            curr = nums[i]
            while monoAsc and curr < nums[monoAsc[-1]]:
                rightSmaller[monoAsc.pop()] = i

            monoAsc.append(i)

        ans = 0
        for i in range(n):
            # only +ve integers need to be turned 0s
            if nums[i] > 0:
                
                if rightSmaller[i] > rb_covered[nums[i]]:
                    ans += 1
                    rb_covered[nums[i]] = rightSmaller[i]

        return ans
    
nums = [1,2,1,2,1,2]
nums = [2,2,2,2,1,2]
nums = [0,2]
nums = [3,1,2,1]

Solution().minOperations(nums)