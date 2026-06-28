# prefix sum - hard
from typing import List
from collections import defaultdict
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        # key ideas:
        # 1) first convert all non-target values to -1 and target values to 1
        # 2) build a prefix sum array based on the converted array
        # 3) perform prefix accounting again on the prefix sum array to
        # compute the number of valid subarrays ending at each index
        pf, pf_sum = [0], 0
        for x in nums:
            pf_sum = pf_sum + 1 if x == target else pf_sum - 1
            pf.append(pf_sum)

        # track prefix sum frequencies
        f = defaultdict(int)
        # first dummy
        f[0] = 1 

        ans, pf_sum = 0, 0
        for i in range(1, len(pf)):
            if pf[i] > pf[i-1]:
                pf_sum += f[pf[i-1]]
            elif pf[i] < pf[i-1]:
                pf_sum -= f[pf[i]]

            ans += pf_sum
            f[pf[i]] += 1

        return ans

nums, target = [1,2,3], 4
nums, target = [1,2,2,3], 2
nums, target = [1,1,1,1], 1

Solution().countMajoritySubarrays(nums, target)