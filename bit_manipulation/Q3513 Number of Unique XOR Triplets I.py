# bit manipulation - medium
from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) given we have all distinct numbers in range [1, n], we can
        # construct all XOR triplets in range [1, 1 << bit_length(n)]
        # 2) to visualise, suppose binary representation of "n" is 1xxxxx,
        # we can form 11111111 as long as the other two numbers occupy the
        # remaining bits exactly with no overlaps (e.g, 0b100000 ^ 0b10001 ^ 0b1110)

        if n <= 2: return n
        return 1 << n.bit_length()

nums = [1,2]
nums = [3,1,2]

Solution().uniqueXorTriplets(nums)