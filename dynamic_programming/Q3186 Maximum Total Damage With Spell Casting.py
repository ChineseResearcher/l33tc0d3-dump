# dp - medium
from typing import List
import bisect
from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        n = len(power)
        # first sort the power to allow binary search later
        power.sort()

        # then we could build a dp arr. with dp[i] init. to power[i]
        dp = [x for x in power]

        # maintain a prefix max. arr. recording max. val up to dp[:i]
        prefix_max = []

        # maintain a ongoing freq counter of numbers
        freq = defaultdict(int)

        for i in range(n):

            freq[power[i]] += 1
            # init. the curr. val to freq of power * power
            curr = freq[power[i]] * power[i]

            # search for earlier dp[j] where power[j] <= power[i] - 3
            j = bisect.bisect_right(power, power[i] - 3)
            if j > 0:
                curr += prefix_max[j-1]

            # update dp val
            if curr > dp[i]:
                dp[i] = curr

            # update prefix_max with the updated dp[i]
            if not prefix_max or prefix_max[-1] < dp[i]:
                prefix_max.append(dp[i])
            else:
                prefix_max.append(prefix_max[-1])

        return prefix_max[-1]
    
power = [7,1,6,6]
power = [1,1,3,4]

Solution().maximumTotalDamage(power)