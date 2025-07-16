# dp - medium
from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        # recognise that for % k, there can be modulo results
        # in the range [0, k-1], thus k possible results

        # since k <= 1000, and nums.length <= 1000, solution would
        # be efficient if it's in O(k * n), and thus we need to work out
        # an O(n) solution for each mod-k
        ans = 0
        for modK in range(k):

            # init. a dp arr. of size k 
            # where dp[i] would represent the length of LIS w/ the last 
            # element x s.t x % k = i
            dp = [0] * k
            for y in range(n):

                modY = nums[y] % k
                # as we want to any two consecutive numbers x, y in the LIS
                # to have (x + y) % k = modK, it is equivalent to 
                # ((x % k) + (y % k) + k) % k = modK (distribution of %)
                modX = (modK - modY + k) % k

                dp[modY] = dp[modX] + 1
                ans = max(ans, dp[modY]) 

        return ans
    
nums, k = [1,2,3,4,5], 2
nums, k = [1,4,2,3,1,4], 3

Solution().maximumLength(nums, k)
    
