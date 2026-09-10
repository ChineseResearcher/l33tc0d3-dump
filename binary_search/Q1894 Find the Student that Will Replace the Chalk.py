# binary search - medium
import bisect
from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        n = len(chalk)
        # key ideas:
        # 1) build prefix sum on chalk array
        # 2) binary search on the prefix sum array to locate the 1st student w/ shortage

        pfSum = [chalk[0]]
        for i in range(1, n):
            pfSum.append(pfSum[-1] + chalk[i])

        k %= pfSum[-1]
        return bisect.bisect_right(pfSum, k)

chalk, k = [5,1,5], 22
chalk, k = [3,4,1,2], 25

Solution().chalkReplacer(chalk, k)