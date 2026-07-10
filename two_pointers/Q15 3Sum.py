# two pointers - medium
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        # key ideas:
        # 1) sort the array 
        # 2) for each nums[i], perform a two-pointer search on [i+1, n-1]
        # to test if we can have triplets where nums[i] + nums[l] + nums[r] = 0
        nums.sort()

        ans = []
        for i, a in enumerate(nums):
            
            # skip duplicate
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r: 
                
                b, c = nums[l], nums[r]
                currSum = a + b + c

                if currSum > 0:
                    r -= 1     
                elif currSum < 0:
                    l += 1  
                else:
                    ans.append([a, b, c])
                    l += 1
                    # skip duplicate
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return ans

nums = [0,0,0]
nums = [0,1,1]
nums = [-1,0,1,2,-1,-4]

Solution().threeSum(nums)