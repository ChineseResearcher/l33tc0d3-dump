# dp - medium
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = int(1e9 + 7)
        # if arr. consists only +ve elements, then ans is sum of all elements * k
        if min(arr) >= 0:
            return (sum(arr) * k) % MOD

        # similarly, for the case of only -ve elements
        if max(arr) < 0:
            return 0

        n = len(arr)
        # first use the solution to maximum subarray problem 
        # to obtain the length-n dp arr., i.e. k = 0

        # kadane's algorithm is a form of DP
        # dp[i] stores the best solution if we consider up to nums[i]
        dp = [0] * n

        dp[0] = arr[0]
        for i in range(1, n):

            # op1: take best solution from dp[i-1] + curr. num
            op1 = dp[i-1] + arr[i]
            # op2: use curr. num only
            op2 = arr[i]

            # choose better option
            dp[i] = max(op1, op2)

        if k == 1:
            return max(dp) % MOD

        # partialMax is the max. subarr sum we can achieve
        # that also guarantees an underlying subarr starting from idx = 0
        partialMax, rSum = 0, 0
        for i in range(n):
            rSum += arr[i]
            partialMax = max(partialMax, rSum)

        # how do we know if we have any potential of improving max(dp)
        # by repeating our seq. to any number of times? test for +ve delta
        delta = sum(arr)

        if delta <= 0:
            return max((max(dp[-1], 0) + partialMax) % MOD, max(dp) % MOD)

        # otherwise, we have improved!
        return (dp[-1] + (k-2) * delta + partialMax) % MOD
    
arr, k = [1,-3,3] * 5, 5
arr, k = [-5,4,-4,-3,5,-3], 3
arr, k = [-5,-2,0,0,3,9,-2,-5,4], 5
arr, k = [-1,1,2,3,-8,4], 2
arr, k = [4,-10,-2,-3,4], 1

Solution().kConcatenationMaxSum(arr, k)