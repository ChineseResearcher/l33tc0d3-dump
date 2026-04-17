# array - medium
from typing import List
from collections import defaultdict
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b

        rev_map = defaultdict(list)
        for i in range(n-1, -1, -1):

            x = nums[i]
            rev_map[x].append(i)

        # helper to obtain the reverse integer
        reverse = lambda x: int(str(x)[::-1].lstrip('0'))

        ans = n
        for i in range(n):
            
            rev_int = reverse(nums[i])
            while rev_map[rev_int] and rev_map[rev_int][-1] <= i:
                rev_map[rev_int].pop()

            if rev_map[rev_int]:
                ans = fmin(ans, rev_map[rev_int][-1] - i)

        return ans if ans < n else -1

nums = [120,21]
nums = [21,120]
nums = [12,21,45,33,54]

Solution().minMirrorPairDistance(nums)