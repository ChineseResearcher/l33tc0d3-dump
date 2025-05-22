# prefix sum - medium
from typing import List
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # the first part of the question is to figure out
        # what are the possible sum ranges if for each pair of numbers
        # only 0, 1, and 2 modifications are allowed?

        # take a pair (1,3) for example, if replace limit = 5
        # then with 0 mod, we can achieve [4,4]
        # w/ 1 mod, we can achieve [(min(1,3)+1 , max(1,3)+5] = [2,8]
        # and for numbers outside [2,8], we would need 2 mods

        # the smallest admissible sum is just 2 * 1, 
        # while the largest admissible sum is 2 * limit

        # the range info corresponding to [0,1,2] mods
        # can be transformed into a "range update" problem
        diff = [0] * (2 * limit + 1)
        m = len(diff)

        for i in range(n // 2):
            
            # retrieve the pair
            a, b = nums[i], nums[n-i-1]
            
            # mark range updates on diff
            diff[2] += 2
            diff[min(a,b)+1] -= 1
            diff[a+b] -= 1
            if a+b+1 < m:    
                diff[a+b+1] += 1
            if max(a,b)+limit+1 < m:
                diff[max(a,b)+limit+1] += 1
            
        # then we carry our running sum of moves across diff
        # and track our ans as the minimum moves required at any point
        ans, acc = float('inf'), 0
        for move in range(2, m):
            
            acc += diff[move]
            ans = min(ans, acc)
            
        return ans
    
nums, limit = [1,2,4,3], 4
nums, limit = [1,2,2,1], 2
nums, limit = [1,2,1,2], 2

Solution().minMoves(nums, limit)

