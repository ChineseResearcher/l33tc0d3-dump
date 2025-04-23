# bst - hard
from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums):
    
        n = len(nums)
        # reverse pairs are pairs (i, j) s.t.
        # 1) i < j 
        # 2) nums[i] > 2 * nums[j]

        # take the perspective of j, and make use of a sortedList
        # to keep all the seen nums[i] in ascending order
        sl = SortedList([])

        ans = 0
        for j in range(n):
            
            ans += len(sl) - sl.bisect_left(2 * nums[j] + 1)
            sl.add(nums[j])
            
        return ans
    
nums = [1,3,2,3,1]
nums = [2,4,3,5,1]

Solution().reversePairs(nums)