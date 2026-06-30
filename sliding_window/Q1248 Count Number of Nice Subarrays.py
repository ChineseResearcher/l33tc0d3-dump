# sliding window - medium
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # key ideas:
        # 1) use a sliding window which tracks odd element count
        # 2) shrink left bound whenever count exceeds k
        # 3) when accounting for nice arrays, we are interested in the
        # index of leftmost odd element in our window [l, r]. Therefore, we need to
        # pre-compute the next odd element index for every odd element.
        nextOdd, prev = dict(), -1
        for i in range(n):
            if nums[i] % 2 == 1:
                nextOdd[prev] = i
                prev = i

        if not nextOdd: return 0

        l, l_odd, ans, oddCnt = 0, nextOdd[-1], 0, 0
        for r in range(n):

            if nums[r] % 2 == 1:
                oddCnt += 1

            # shrink window
            while oddCnt > k:
                if nums[l] % 2 == 1:
                    oddCnt -= 1
                l += 1

            # move pointer to the leftmost odd element
            while l_odd < l:
                l_odd = nextOdd[l_odd]

            # validate nice array
            if oddCnt == k:
                ans += (l_odd - l + 1)

        return ans

nums, k = [2,4,6], 1
nums, k = [1,1,2,1,1], 3
nums, k = [2,2,2,1,2,2,1,2,2,2], 2

Solution().numberOfSubarrays(nums, k)