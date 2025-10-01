# bit manipulation - hard
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        # init. an array storing count of i-th bit
        bc, subarrOR = [0] * 31, 0

        def getOR(bit_cnt: List[int]):
            res = 0
            for bit in range(31):
                if bit_cnt[bit] > 0:
                    res += (1 << bit)

            return res

        l, ans = 0, float('inf')
        for r in range(n):

            # increment subarr OR bit cnt
            for bit in range(nums[r].bit_length()):
                if (1 << bit) & nums[r] != 0:
                    bc[bit] += 1

            subarrOR = getOR(bc)
            ans = min(ans, abs(k - subarrOR))

            # shrink the window if subarrOR exceeds k
            while l <= r and subarrOR > k:

                # decrement subarr OR bit cnt
                for bit in range(nums[l].bit_length()):
                    if (1 << bit) & nums[l] != 0:
                        bc[bit] -= 1

                subarrOR = getOR(bc)
                l += 1

                if l <= r:
                    ans = min(ans, abs(k - subarrOR))
                
        return ans
    
nums, k = [1], 10
nums, k = [1,10], 6
nums, k = [1,2,4,5], 3
nums, k = [1,3,1,3], 2

Solution().minimumDifference(nums, k)