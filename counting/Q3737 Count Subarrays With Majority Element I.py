# counting - medium
from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        # key idea:
        # 1) brute-force and check majority by tracking frequency

        ans = 0
        for i in range(n):
            f = 0
            for j in range(i, n):
                if nums[j] == target: f += 1
                # majority checking
                if f > (j-i+1) >> 1:
                    ans += 1

        return ans
    
nums, target = [1,2,3], 4
nums, target = [1,2,2,3], 2
nums, target = [1,1,1,1], 1

Solution().countMajoritySubarrays(nums, target)