# dp - medium
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        # key ideas:
        # 1) a natural state transition exists because of the requirement
        # to have a lexicographically sorted string
        # 2) for each letter in (a, e, i, o, u), at index i, the number of
        # formations is equal to dp[i-1][c] s.t. c <= curr. character
        dp = [1] * 5

        for _ in range(1, n):
            new_dp = [0] * 5
            for j in range(5):
                for k in range(j+1):
                    new_dp[j] += dp[k]

            dp = new_dp

        return sum(dp)
    
n = 1
n = 2
n = 33
n = 50 # constraint

Solution().countVowelStrings(n)