# sliding window - medium
from typing import List
from collections import deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # key ideas:
        # 1) we use two monotonic queues to maintain sliding window max / min
        # 2) keep shifting left end of window if cost exceeds k

        def cost(winMax:int, winMin:int) -> int:
            '''
            Compute window cost based on window Max / Min and [l, r]
            '''
            return (winMax - winMin) * (r - l + 1)

        Max, Min = deque(), deque()

        l, ans = 0, 0
        for r, x in enumerate(nums):

            while Max and x > Max[-1]:
                Max.pop()
            Max.append(x)

            while Min and x < Min[-1]:
                Min.pop()
            Min.append(x)

            # shrink left end if needed
            while cost(Max[0], Min[0]) > k:
                if Max[0] == nums[l]:
                    Max.popleft()
                if Min[0] == nums[l]:
                    Min.popleft()
                l += 1

            ans += (r - l + 1)

        return ans

nums, k = [1,3,2], 4
nums, k = [1,2,3], 0
nums, k = [5,5,5,5], 0

Solution().countSubarrays(nums, k)