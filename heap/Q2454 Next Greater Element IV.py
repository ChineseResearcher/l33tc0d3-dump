# heap - hard
from typing import List
import heapq
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # stack storing indices of a non-increasing seq.
        st = []

        # build an auxiliary rightMax array where rm[i] stores the max from nums[i...n]
        rm = [0] * n
        rm[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            rm[i] = max(rm[i+1], nums[i])

        ans, minheap = [-1] * n, []
        for idx, num in enumerate(nums):

            # first explore if the curr. number can be the second greater
            # element of those who have already found a first greater element
            while minheap and num > minheap[0][0]:
                _, found_idx = heapq.heappop(minheap)
                ans[found_idx] = num

            # then continue building the monoStack w/ curr number
            while st and num > nums[st[-1]]:
                smaller_idx = st.pop()
                # funnel into the minheap only if it has a second greater element
                if idx < n-1 and rm[idx+1] > nums[smaller_idx]:
                    heapq.heappush(minheap, [nums[smaller_idx], smaller_idx])

            st.append(idx)
            
        return ans
    
nums = [3,3]
nums = [2,4,0,9,6]
nums = [2,4,0,9,3,6]
nums = [3,11,19,6,4,6,14,1,11,9]
nums = [11,13,15,12,0,15,12,11,9]

Solution().secondGreaterElement(nums)