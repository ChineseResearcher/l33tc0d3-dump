# greedy - hard
MOD = int(1e9) + 7
from typing import List
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        D = max(nums).bit_length()
        # key ideas:
        # 1) use an array of size equal to the bit length of max(nums)
        # as an counter of the number of set bits at each position
        # 2) iterate through nums array (up to the k-th), and make each number
        # as big as possible by shifting set bits to empty bits of curr. number
        bit = [0] * D

        for x in nums:
            for i in range(x.bit_length()):
                if x & (1 << i):
                    bit[i] += 1

        ans = 0
        for i in range(k):

            x = nums[i]
            rx = x
            for j in range(x.bit_length()):
                if x & (1 << j):
                    # reduce x by unsetting exhausted bits
                    if bit[j] == 0:
                        rx &= ~(1 << j)
                    # exclude set bits
                    else:
                        bit[j] -= 1

            nx = rx
            # make nx as big as possible by borrowing bits via bitwise OR
            for j in range(D):
                if not nx & (1 << j) and bit[j] > 0:
                    nx |= (1 << j)
                    # shifted 1 set bit to curr. position, and
                    # also reduced total cnt of this position by one
                    # due to annihilation of bitwise AND
                    bit[j] -= 1 

            ans += pow(nx, 2, MOD)
            ans %= MOD

        return ans

nums, k = [2,6,5,8], 2
nums, k = [4,5,4,7], 3
nums, k = [25,52,75,65], 4

Solution().maxSum(nums, k)