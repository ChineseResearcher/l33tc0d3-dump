# dp - hard
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        # 3D dp : dp[index][divisor][remainder]
        # optimised into 2D dp as we only need the dict at the prev. index
        dp = [[0] * i for i in range(10)]

        ans = 0
        for i in range(n):

            curr_digit = int(s[i])
            new_dp = [[0] * i for i in range(10)]

            for d in range(1, 10):
                new_dp[d][curr_digit % d] += 1

            # inheritance enabled
            if i > 0:
                for d in range(1, 10):
                    for rem in range(0, d):

                        # reasoning: suppose s[:i] = '1293'
                        # if we want to know 1293 % k,
                        # we can break it down into :
                        # ( (1290 % k) + (3 % k) ) % k
                        # equivalently, ( ((129 % k) * (10 % k)) % k + (3 % k) ) % k
                        new_rem = (rem * 10 + curr_digit) % d
                        new_dp[d][new_rem] += dp[d][rem]

            dp = new_dp # space optimisation by override

            if curr_digit > 0:
                ans += new_dp[curr_digit][0]

        return ans
    
s = "12936"
s = "5701283"
s = "1010101010"
s = "10" * (int(1e5) // 2) # constraint

Solution().countSubstrings(s)