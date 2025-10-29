# dp - hard
from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        n = len(target)
        # use monotonic stack to build a leftSmaller arr.
        leftSmaller, monoAsc = [-1] * n, []

        for i in range(n-1, -1, -1):

            while monoAsc and target[i] < target[monoAsc[-1]]:
                leftSmaller[monoAsc.pop()] = i

            monoAsc.append(i)

        # find the answer using dp + pre-computed leftSmaller
        dp = [0] * n
        dp[0] = target[0] # init. first val

        for i in range(1, n):
            # determine if target[i] has a valid leftSmaller
            if leftSmaller[i] > -1:

                j = leftSmaller[i]
                # compute the cost with leftSmaller as a constraint
                constrained_op = dp[j] + (target[i] - target[j])

                # compare with dp[-1]
                if dp[i-1] > constrained_op:
                    constrained_op = dp[i-1]

                dp[i] = constrained_op

            else:
                dp[i] = dp[i-1]

        return dp[-1]
    
target = [1,2,3,2,1]
target = [3,1,1,2]
target = [3,1,5,4,2]

Solution().minNumberOperations(target)