# sorting - medium
from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        # goal is to construct exactly n // 3 subarrays w/ no
        # subarray having a group diff larger than k

        # applying greedy thinking, the closest numbers should get
        # grouped first so we could sort the nums arr.
        nums.sort()

        ans = []
        for i in range(0, n, 3):

            # the consecutive three elements form an ideal grp
            m1, m2, m3 = nums[i], nums[i+1], nums[i+2]
            if m3 - m1 > k:
                return []

            ans.append([m1,m2,m3])

        return ans
    
nums, k = [1,3,4,8,7,9,3,5,1], 2
nums, k = [2,4,2,2,5,2], 2
nums, k = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14

Solution().divideArray(nums, k)