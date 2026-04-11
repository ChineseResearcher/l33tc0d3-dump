# array - medium
from typing import List
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) best tuple can be greedily identified by always choosing
        # elements that are the closest to one another
        # 2) use a hashmap to record the indices for every unique number
        pos = defaultdict(list)

        for idx, x in enumerate(nums):
            pos[x].append(idx)

        ans = float('inf')
        for i_arr in pos.values():
            if len(i_arr) < 3:
                continue

            for idx in range(len(i_arr)-2):
                i, j, k = i_arr[idx], i_arr[idx+1], i_arr[idx+2]
                ans = fmin(ans, (j-i) + (k-j) + (k-i))

        return ans if ans < float('inf') else -1

nums = [1,2,1,1,3]
nums = [1,1,2,3,2,1,2]

Solution().minimumDistance(nums)