# bst - hard
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums):
        
        # we would leverage on inherent BST in SortedList
        # to efficiently search/remove in O(logN) time
        sl = SortedList(nums)

        counts = [0] * len(nums)
        for i in range(len(nums)):
            
            counts[i] = sl.bisect_left(nums[i])
            # remove nums[i]
            sl.remove(nums[i])
            
        return counts
    
nums = [5,2,6,1]
nums = [-1]
nums = [-1,-1]

Solution().countSmaller(nums)