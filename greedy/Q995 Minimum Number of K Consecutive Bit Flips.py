# greedy - hard
from typing import List
from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) simulate the flipping process using a queue 
        # 2) use differencing technique to obtain the number of flips at each index
        diff = [0] * n

        q, idx, curr_flips, ans = deque(), 0, 0, 0
        while True:

            while len(q) < k and idx < n:
                q.append(idx)
                idx += 1

            # if we cannot recruit k members, early exit
            if len(q) < k:
                if len(q) > 0:
                    curr_flips += diff[q[0]]
                    while q and (nums[q[0]] + curr_flips) & 1 == 1:
                        q.popleft()
                        if q: curr_flips += diff[q[0]]
                    # curr_flips is nonzero, indicating unfinished flip
                    if q or curr_flips > 0: ans = -1
                break
            
            curr_flips += diff[q[0]]
            # clear elements as long as they successfully 
            # turn into "1" after prescribed number of flips
            # note: there's a bitwise optimisation trick here,
            # instead of checking if total_flip % 2 == 1, use bitwise &
            while q and (nums[q[0]] + curr_flips) & 1 == 1:
                q.popleft()
                if q: curr_flips += diff[q[0]]

            if q:
                # if q is not emptied, we've encountered a "0"
                diff[q[0]] = 1
                if q[0] + k < n:
                    diff[q[0] + k] -= 1

                # one more flip needed
                ans += 1

        return ans

nums, k = [1,0], 2
nums, k = [0,1,0], 1
nums, k = [1,1,0], 2
nums, k = [1,1,1], 2
nums, k = [0,0,1], 2
nums, k = [1,0,0,0,0], 2
nums, k = [0,0,1,0,1,1,0], 4
nums, k = [0,0,0,1,0,1,1,0], 3

Solution().minKBitFlips(nums, k)