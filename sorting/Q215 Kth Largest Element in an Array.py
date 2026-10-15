# sorting - medium
from collections import defaultdict
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) the range of possible values is small, [-1e4, 1e4]
        # 2) counting sort on the min / max range of nums

        a, b = float('inf'), float('-inf')
        f = defaultdict(int)
        for x in nums:
            a = fmin(a, x)
            b = fmax(b, x)
            f[x] += 1

        pfCnt, k = 0, len(nums) - k + 1
        for v in range(a, b + 1):
            pfCnt += f[v]
            if pfCnt >= k:
                return v

nums, k = [3,2,1,5,6,4], 2
nums, k = [3,2,3,1,2,4,5,5,6], 4

Solution().findKthLargest(nums, k)