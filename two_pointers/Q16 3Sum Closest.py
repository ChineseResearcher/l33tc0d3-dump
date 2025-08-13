# two - pointers
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # core ideas:
        # 1) sort nums and use two pointer to locate a trio of numbers
        # 2) minimise the absolute difference to the target
        nums.sort()

        def closest(curr, best):

            if abs(curr - target) < abs(best - target):
                return curr
            
            return best

        ans = float('inf')
        for k in range(n-2):
            
            i, j = k + 1, n - 1
            while i < j:

                curr = nums[k] + nums[i] + nums[j]
                ans = closest(curr, ans)

                if curr < target:
                    i += 1
                elif curr > target:
                    j -= 1
                else:
                    return curr

        return ans
    
nums, target = [-1,2,1,-4], 1
nums, target = [0,0,0], 1
nums, target = [4,0,5,-5,3,3,0,-4,-5], -2
nums, target = [0,1,2], 3

Solution().threeSumClosest(nums, target)