# two pointers - hard
from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        n = len(nums)
        # to make an arr increasing after removing subarr arr[l..r]
        # we have to make sure:
        # (1) arr[0..l-1] are strictly increasing
        # (2) arr[r+1...n-1] are strictly increasing
        # (3) arr[l-1] < arr[r+1]

        # the core idea is to approach w/ two pointers
        # first pointer x is the index s.t. arr[0...x] is strictly increasing
        # second pointer y is the index s.t. arr[y...n-1] is strictly increasing
        x = 0
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                break
            x = i

        y = n-1
        for j in range(n-2, -1, -1):
            if nums[j] >= nums[j+1]:
                break
            y = j

        # special case: nums is already strictly increasing
        if y <= x:
            return n * (n + 1) // 2

        # first init. ans based on y
        # e.g. for nums [3,2,1,2,3,4]
        # because y = 2, we could delete [3,2], [3,2,1], [3,2,1,2], [3,2,1,2,3], [3,2,1,2,3,4]
        # to make the remaining nums arr. strictly increasing
        ans = n - y + 1
        for i in range(x+1):

            while y < n and nums[y] <= nums[i]:
                y += 1
            ans += n - y + 1

        return ans
    
nums = [1,2,3,4]
nums = [6,5,7,8]
nums = [8,7,6,6]

Solution().incremovableSubarrayCount(nums)