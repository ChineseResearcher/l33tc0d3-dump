# two pointers - medium
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, a in enumerate(nums):
            
            # if we see a repeated num we skip as we only want unique triplets
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r: 
                
                triplet_sum = a + nums[l] + nums[r]
    
                # think of a shrinking sliding window across a list of sorted numbers
                # s.t. i < (l, r) < len(nums) 
                if triplet_sum > 0:
                    r -= 1     
                elif triplet_sum < 0:
                    l += 1  
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    # again, skip repeated numbers
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return ans

nums = [0,0,0]
nums = [0,1,1]
nums = [-1,0,1,2,-1,-4]

Solution().threeSum(nums)