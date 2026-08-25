# binary search - medium
import bisect
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # key ideas:
        # 1) we are only interested in the length of the LIS, binary 
        # search on the curr. best subsequence to determine placement of
        # a new element

        best_seq = []
        for x in nums:
            i = bisect.bisect_left(best_seq, x)
            if i == len(best_seq):
                best_seq.append(x)
            else:
                best_seq[i] = x

        return len(best_seq)

nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
nums = [10,9,2,5,3,7,101,18]

Solution().lengthOfLIS(nums)