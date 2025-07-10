# dp - medium
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        n = len(arr)

        # construct dp of size 2 x n
        # where 2 denotes (False, True) for deletion status
        dp = [ [0] * n for _ in range(2) ]

        dp[0][0] = arr[0]
        dp[1][0] = 0
        
        # ans. cannot be init. to dp[1][0] because we require
        # a subarr. to be non-empty
        ans = dp[0][0]
        for i in range(1, n):
            
            # to have deletion status at i to be False:
            # 1) inherit from previous False (i.e. dp[0][i-1]) and still add arr[i]
            # 2) re-start the subarr. at arr[i] -> key to solving Maximum Subarr. Sum
            dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])

            # to have deletion status at i to be True:
            # 1) inherit from previous True (i.e. dp[1][i-1]) and still add arr[i]
            # 2) inherit from previous False (i.e. dp[0][i-1]) and skip arr[i]
            dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

            ans = max(ans, max(dp[0][i], dp[1][i]))

        return ans
    
arr = [1,-2,0,3]
arr = [1,-2,-2,3]
arr = [-1,-1,-1,-1]
arr = [2,1,-2,-5,-2]

Solution().maximumSum(arr)