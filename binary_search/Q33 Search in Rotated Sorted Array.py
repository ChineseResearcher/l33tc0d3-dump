# binary search - medium
import bisect
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l0, r0 = nums[0], nums[-1]

        if target == l0: return 0
        if target == r0: return n-1

        # array is not rotated if l0 < r0
        if l0 < r0:
            i = bisect.bisect_left(nums, target)
            return i if i < n and nums[i] == target else -1

        # for an rotated array,
        # the target (if exists) is EITHER in
        # [nums[k], nums[k+1], ..., nums[n-1]]
        # OR [nums[0], nums[1], ..., nums[k-1]]

        # we perform binary search with different logics 
        # depending on which section the target potentially lies in
        if target > l0:

            l, r = 0, n-1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    if nums[mid] >= l0:
                        l = mid + 1
                    elif nums[mid] <= r0:
                        r = mid - 1
                else:
                    r = mid - 1

        elif target < r0:
            
            l, r = 0, n-1
            while l <= r:

                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    if nums[mid] >= l0:
                        l = mid + 1
                    elif nums[mid] <= r0:
                        r = mid - 1
                else:
                    l = mid + 1

        return -1
    
nums, target = [4,5,6,7,0,1,2], 0
nums, target = [4,5,6,7,0,1,2], 3

Solution().search(nums, target)