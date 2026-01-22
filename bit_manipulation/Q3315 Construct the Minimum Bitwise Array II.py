# bit manipulation - medium
from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
   
        # key ideas:
        # 1) the operation of a OR (a+1) is essentially taking the first
        # 0-bit to the left of trailing 1-bits and flip it to 1

        # 2) for a number to have an answer, i.e. can be formed by some
        # a OR (a+1), it must have at least 1 trailing 1
        # note: 0b110110 does not have trailing 1-bit

        ans = []
        for x in nums:

            if x & (1 << 0) == 0:
                ans.append(-1)
                continue

            idx = 0
            while True:

                # locate the first 0-bit to the left
                # of trailing 1-bit(s), and unset the idx-1 bit
                if x & (1 << idx) == 0:
                    x &= ~(1 << (idx-1))
                    break
                idx += 1

            ans.append(x)

        return ans
    
nums = [2,3,5,7]
nums = [11,13,31]

Solution().minBitwiseArray(nums)