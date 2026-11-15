# sliding window - medium
from collections import deque
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) use of monotonic queues to maintain window max & min
        # 2) shrink window left end when window max - window min exceeds 2
        wmax, wmin = deque(), deque()

        l, ans = 0, 0
        for r in range(n):

            x = nums[r]
            while wmax and x > nums[wmax[-1]]:
                wmax.pop()
            wmax.append(r)

            while wmin and x < nums[wmin[-1]]:
                wmin.pop()
            wmin.append(r)
            
            # shrink window
            while nums[wmax[0]] - nums[wmin[0]] > 2:
                l += 1
                while wmax[0] < l:
                    wmax.popleft()
                while wmin[0] < l:
                    wmin.popleft()

            ans += (r - l + 1)

        return ans

nums = [1,2,3]
nums = [5,4,2,4]

Solution().continuousSubarrays(nums)