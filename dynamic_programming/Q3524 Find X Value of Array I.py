# dp - medium
from typing import List
from functools import cache
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        # key ideas:
        # 1) solve top-down DP with states (i, currMod) with a take/skip approach
        # 2) currMod is init. to -1 as dummy to indicate that the seq. has not started
        # 3) at each recursion, we return a list of integers of size k (note k <= 5)

        @cache
        def f(i: int, currMod: int) -> List[int]:

            # if currMod is already 0, it will not change to any other
            # mod values in range [1, k - 1], so we early return
            if currMod == 0:
                res = [0] * k
                # accounting based on curr. index
                res[0] += n - i + 1
                return res

            res = [0] * k
            # treat. curr index as the end -> suffix [i...n] removed
            if currMod != -1:
                res[currMod] += 1

            if i == n:
                return res

            # if seq. has not started, we can skip OR take
            if currMod == -1:
                skip = f(i + 1, currMod)
                take = f(i + 1, nums[i] % k)
                for j in range(k):
                    res[j] += skip[j] + take[j]
            else:
                take = f(i + 1, (currMod * (nums[i] % k)) % k)
                for j in range(k):
                    res[j] += take[j]

            return res

        return f(0, -1)

nums, k = [1,1,2,1,1], 2
nums, k = [1,2,3,4,5], 3
nums, k = [1,2,4,8,16,32], 4

Solution().resultArray(nums, k)