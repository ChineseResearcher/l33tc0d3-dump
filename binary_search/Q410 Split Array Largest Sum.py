# binary search - hard
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # build prefix sum
        pfSum, rSum = [], 0
        for num in nums:
            
            rSum += num
            pfSum.append(rSum)

        if k == 1:
            return pfSum[-1]

        def canDivide(target:int) -> bool:
            
            # given a target max subarr sum, see if we can
            # split in nums arr. in such a way that no subarray sum exceeds target
            
            # maintain a running curr. subarray sum
            # track the number of partitions used
            css, pu = 0, 0
            for i in range(len(nums)):
                
                css += nums[i]
                if css > target:
                    
                    pu += 1
                    css = nums[i]
                    if pu == k-1:
                        break
                        
            # check whether the sum from last partition onwards
            # would sum up to be smaller or equal to target
            return (pfSum[-1] - pfSum[i-1]) <= target

        # binary search on our answer with the smallest possible
        # target being the max(nums), and biggest being sum(nums)
        l, r = max(nums), sum(nums)

        ans = float('inf')
        while l <= r:
            
            target = (l + r) // 2
            if canDivide(target):
                ans = min(ans, target)
                r = target - 1
                
            else:
                l = target + 1
                
        return ans
    
nums, k = [7,2,5,10,8], 2
nums, k = [1,2,3,4,5], 2
nums, k = [1,2,3,4,5], 1

Solution().splitArray(nums, k)