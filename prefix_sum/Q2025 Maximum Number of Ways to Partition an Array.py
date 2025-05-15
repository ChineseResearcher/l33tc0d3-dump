# prefix sum - hard
from typing import List
from collections import deque, defaultdict
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        # there are maximally n-1 partitions possible 
        # for partition going from idx = 1 to idx = n-1

        # build a prefix sum to facilitate subarray sum calculation
        pfSum, rSum = [], 0

        # also manages a hashmap storing indices for each unique running sum
        # i.e. running-sum hashmap (rsh)
        # Note: deque is used for lazy-deletions
        rsh = dict()

        for i in range(n):
            
            rSum += nums[i]
            pfSum.append(rSum)
            
            if i < n-1:
                if rSum not in rsh:
                    rsh[rSum] = deque([])
                rsh[rSum].append(i)
            
        # to make left & right sum balanced, it's important to realise
        # that pfSum[i-1] = pfSum[-1] - pfSum[i-1]
        # equivalently, if pfSum[i-1] = pfSum[-1] // 2, 
        # we've found a balanced partition

        # ans can be initiated to the number of 
        # pfSum[i] s.t. pfSum[i] = pfSum[-1] // 2
        if pfSum[-1] % 2 != 0 or pfSum[-1] // 2 not in rsh:
            ans = 0
        else:
            ans = len(rsh[pfSum[-1] // 2])

        # explore how does changing nums[p] to k would improve ans
        lrsh = defaultdict(int)
        for p in range(n):

            if p > 0:
                lrsh[pfSum[p-1]] += 1

            delta = k - nums[p]
            if (pfSum[-1] + delta) % 2 != 0:
                continue
                
            targetSum = (pfSum[-1] + delta) // 2 - delta

            r_cnt = 0
            if targetSum in rsh:
                while rsh[targetSum] and rsh[targetSum][0] < p:
                    rsh[targetSum].popleft()

                r_cnt = len(rsh[targetSum])

            l_cnt = lrsh[(pfSum[-1] + delta) // 2]
            ans = max(ans, l_cnt + r_cnt)
            
        return ans
    
nums, k = [2,-1,2], 3
nums, k = [0,0,0], 1
nums, k = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], -33
nums, k = [0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,00,0,0,0], 0
nums, k = [0,0,0,0,0,0,0,0,0,-4732,0,0,0,0,0,0,0,0,0], -4732

Solution().waysToPartition(nums, k)