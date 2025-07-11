# bit manipulation - medium
from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
   
        def get_set_bits(num: int) -> List[int]:

            # given a 10-based number, record the set
            # bits' positions in an arr

            idx = 0
            res = []
            while (1 << idx) <= num:
                if num & (1 << idx) != 0:
                    res.append(idx)

                idx += 1

            return res

        ans = []
        for num in nums:

            sb = get_set_bits(num)
            # create a mask to explore potential candidates
            # s.t. mask | (mask - 1) = num
            mask = 0

            curr_ans = float('inf')
            for i in range(len(sb)-1, -1, -1):
                
                mask |= (1 << sb[i])
                # mask explored will be from smaller to bigger
                # as we are including more set bits in the left common region
                if (mask | (mask - 1)) == num:
                    curr_ans = min(curr_ans, mask - 1) # we need to minimise ans[i]

            ans.append(curr_ans if curr_ans < float('inf') else -1)

        return ans
    
nums = [2,3,5,7]
nums = [11,13,31]

Solution().minBitwiseArray(nums)