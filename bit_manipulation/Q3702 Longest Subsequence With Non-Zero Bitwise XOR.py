# bit manipulation
from typing import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        # key ideas:
        # 1) XOR annihilates itself when both values are equal
        # 2) pre-process the nums array to remove any 0s, and keep its count
        # 3) for the filtered nums, suppose its length is n, the longest
        # subsequence with non-zero XOR is either n or n - 1

        fnums, z = [], 0
        for x in nums:
            if x == 0:
                z += 1
            else:
                fnums.append(x)

        if not fnums: return 0

        n, curr_xor = len(fnums), fnums[0]
        for i in range(1, n):
            curr_xor ^= fnums[i]

        k = n if curr_xor > 0 else n - 1
        return k + z

nums = [0,7]
nums = [1,2,3]
nums = [2,3,4]
nums = [7,6,1,9]

Solution().longestSubsequence(nums)