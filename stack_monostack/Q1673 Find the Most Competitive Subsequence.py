# monotonic stack - medium
from typing import List
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # maintain a monotonically increasing stack
        st = [nums[0]]

        for i in range(1, n):
            
            # note: because we want length-k largest number
            # there's additional check on whether st[-1] can be popped
            while st and nums[i] < st[-1] and len(st) + (n-i-1) >= k:
                st.pop()

            # append the larger number
            st.append(nums[i])

        # trim off additional nums
        while len(st) > k:
            st.pop()

        return st
    
nums, k = [3,5,2,6], 2
nums, k = [2,4,3,3,5,4,9,6], 4

Solution().mostCompetitive(nums, k)