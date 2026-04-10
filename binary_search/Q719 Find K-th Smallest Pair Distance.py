# binary search - hard
import bisect
from typing import Tuple, List
from collections import Counter
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        # key ideas:
        # 1) binary search on the answer (k-th smallest dist.)
        # 2) for a certain target, we can compute the count of paired dist. that are
        # smaller to equal to target, in O(n*logn) time assuming nums are already sorted
        nums.sort()

        # helper to return the count of dist. smaller or equal to
        # "target", and the count of dist exactly equal to "target"
        def get_cnt(target:int) -> Tuple[int, int]:

            c = Counter(nums)
            se_cnt, exact_cnt = 0, 0
            for i, x in enumerate(nums):

                exact_cnt += c[x+target]
                if target == 0:
                    exact_cnt -= 1

                # use binary search to locate rightmost index
                j = bisect.bisect_right(nums, x + target)
                se_cnt += j - i - 1

                c[x] -= 1

            return se_cnt, exact_cnt

        # right bound for binary search on answer is determined by
        # the biggest pair dist. possible: nums[-1] - nums[0]
        l, r = 0, nums[-1] - nums[0]
        while l <= r:

            t = (l + r) // 2
            se_cnt, exact_cnt = get_cnt(t)
            if se_cnt < k:
                l = t + 1
            else:
                if exact_cnt == 0:
                    r = t - 1
                    continue

                if k > se_cnt - exact_cnt:
                    # found answer
                    return t
                else:
                    r = t - 1

        return -1
    
nums, k = [1,3,1], 3
nums, k = [1,1,1], 2
nums, k = [1,2,3,3,4,5], 15

Solution().smallestDistancePair(nums, k)