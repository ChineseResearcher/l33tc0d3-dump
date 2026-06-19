# greedy - medium
from typing import List
class Solution:
    def minDeletion(self, nums: List[int]) -> int:

        n = len(nums)
        # key ideas:
        # 1) use a stack to store the final elements as we process 
        # the nums array from left to right
        # 2) skip elements in nums when there is a violation
        st = []

        ans = 0
        for i in range(n):
            # no restriction at odd indices
            if len(st) % 2 == 0:
                st.append(nums[i])
            else:
                if nums[i] != st[-1]:
                    st.append(nums[i])
                else:
                    ans += 1 # skip / discard nums[i]

        if len(st) % 2 == 1: ans += 1
        return ans
    
nums = [1,1,2,3,5]
nums = [1,1,2,2,3,3]

Solution().minDeletion(nums)