# dp - medium
from collections import deque
from typing import List
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # key ideas:
        # 1) use max / min monotonic queues to maintain valid sliding window
        # 2) use prefix sum on dp to obtain count for subproblem up to index i

        dp, pf_dp, pfSum = [0] * n, [], 0
        minQ, maxQ = deque([]), deque([])

        MOD, l = int(1e9 + 7), 0 
        for r in range(n):

            while maxQ and nums[r] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(r)

            while minQ and nums[r] < nums[minQ[-1]]:
                minQ.pop()
            minQ.append(r)

            # shrink window if min-max diff. exceed k
            while nums[maxQ[0]] - nums[minQ[0]] > k:
                if nums[l] == nums[maxQ[0]]:
                    maxQ.popleft()
                if nums[l] == nums[minQ[0]]:
                    minQ.popleft()

                l += 1
            
            # the count for dp[r] follows the transition:
            # dp[r] = dp[l-1] + dp[l] + dp[l+1] + ... + dp[r-1]

            # optimisation by prefix sum: 
            # where dp[r] = prefixSum(r-1) - prefixSum(l-2)
            if r-1 == -1:
                pf_r = 0
            else:
                pf_r = pf_dp[r-1]

            if l-2 == -2:
                pf_l = -1
            elif l-2 == -1:
                pf_l = 0
            else:
                pf_l = pf_dp[l-2]

            dp[r] += pf_r - pf_l
            dp[r] %= MOD

            pfSum += dp[r]
            pf_dp.append(pfSum)

        return dp[-1]

nums, k = [9,4,1,3,7], 4
nums, k = [3,3,4], 0
nums, k = [12,13,7], 6

Solution().countPartitions(nums, k)