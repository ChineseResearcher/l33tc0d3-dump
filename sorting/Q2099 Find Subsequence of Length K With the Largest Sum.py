# sorting - easy
from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        num_idx = [[num, idx] for idx, num in enumerate(nums)]
        # what's easily confused is that while the order matters
        # if we just take the largest k numbers, they are surely a valid subseq.
        # it's just we need to express it in-order only
        num_idx = sorted(num_idx, key=lambda x: x[0], reverse=True)[:k] # only k needed
        select_idx = sorted(num_idx, key=lambda x: x[1]) # sort chosen k items by their indices

        return [x[0] for x in select_idx]
    
nums, k = [2,1,3,3], 2
nums, k = [-1,-2,3,4], 3
nums, k = [3,4,3,3], 2
nums, k = [50,-75], 2
nums, k = [-8,-94,-30,-98,-27,62,26], 7

Solution().maxSubsequence(nums, k)
    
