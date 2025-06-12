# binary search - medium
from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def canForm(target, nums, p):

            # given a target mini-max abs diff, greedily try
            # if we can form at least p pairs not exceeding this target
            n = len(nums)

            i, formed = 0, 0
            while i < n-1:

                if abs(nums[i] - nums[i+1]) <= target:
                    formed += 1
                    i += 2 # skip the pair
                else:
                    i += 1

                if formed >= p:
                    return True
                
            return False

        # binary search on the mini-max abs diff amongst p pairs
        l, r = 0, nums[-1]-nums[0]

        while l <= r:

            mid = (l + r) // 2
            if canForm(mid, nums, p):
                r = mid - 1
            else:
                l = mid + 1

        return l
    
nums, p = [10,1,2,7,1,3], 2
nums, p = [4,2,1,2], 1
nums, p = [3,4,2,3,2,1,2], 3

Solution().minimizeMax(nums, p)