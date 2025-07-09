# greedy - medium
from typing import List
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1] if n > 1 else -1
        if n == 1:
            return nums[0] if k % 2 == 0 else -1

        ans = -1
        for idx, num in enumerate(nums):
            
            # it takes idx moves at least to get curr. num to be leftmost
            # 1) pop exactly idx times to surfact curr. num
            # 2) pop at least idx + 1 times s.t. curr. num is included in the
            # removed set and insert back 
            if num > ans:
                if k == idx:
                    ans = num

                choice = idx + 1
                if k > idx + 1:

                    # it is important to realise that if we are making "choice" popping moves
                    # to inlcude curr. num in removed set, and this move cnt > 1, then we will
                    # always be able to insert curr. num as the topmost element
                    if choice > 1:
                        ans = num

                    # if curr. num happens to be the first number in nums arr.
                    # and that there are other elements in nums arr.
                    # it can be treated as the case of "choice > 1"
                    elif choice == 1 and choice < n:
                        ans = num

        return ans
    
nums, k = [5,2,2,4,0,6], 4
nums, k = [2], 1
nums, k = [18], 3
nums, k = [99,95,68,24,18], 69
nums, k = [73,63,62,16,95,92,93,52,89,36,75,79,67,60,42,93,93,74,94,73,35,86,96], 59
nums, k = [0], 1000000000

Solution().maximumTop(nums, k)