# number theory - medium
import math
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        # key ideas:
        # 1) we can do this is O(1) space
        # 2) for any index i, we can start circular swapping
        # until it hit M steps
        # 3) M = LCA(k % n, n) // (k % n)
        # 4) keep track of total swap count, and break when it reaches n
        k %= n
        if k == 0: return nums

        M = math.lcm(k, n) // k
        i, cnt = n - k, 0
        while cnt < n:

            step = 0
            j, new = (i + k) % n, nums[i]
            while step < M:
                # in-place swap
                t = nums[j]
                nums[j] = new
                new = t
                # jump again
                j = (j + k) % n
                # increment step & count
                step += 1
                cnt += 1

            # move starting index
            i += 1

        return nums

nums, k = [1,2], 7
nums, k = [1,2,3,4,5,6], 4
nums, k = [-1,-100,3,99], 2
nums, k = [1,2,3,4,5,6,7], 3

Solution().rotate(nums, k)