# dp - medium
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        n = len(arr)
        MOD = int(1e9 + 7)

        dp = [0] * (n + 1)
        # initiate the dp val. for the first number depending on parity
        dp[1] = 1 if arr[0] % 2 == 1 else 0

        for i in range(1, n):
            # find the number of odd-sum subarrs. ending at arr[i-1]
            prev_odd_subarr = dp[i] - dp[i - 1]
            # find the number of even-sum subarrs. ending at arr[i-1]
            prev_even_subarr = i - prev_odd_subarr

            # 1) curr. arr[i] being odd allows it to inherit prev_even_subarr
            if arr[i] % 2 == 1:
                # +1 as [arr[i]] is also odd-subarray
                dp[i + 1] = (dp[i] + prev_even_subarr + 1) % MOD
            # 2) curr. arr[i] being even allows it to inherit prev_odd_subarr
            else:
                dp[i + 1] = (dp[i] + prev_odd_subarr) % MOD

        return dp[-1] % MOD
    
arr = [1,3,5]
arr = [2,4,6]
arr = [1,2,3,4,5,6,7]

Solution().numOfSubarrays(arr)