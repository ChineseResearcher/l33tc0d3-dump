# dp - hard
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        MOD = int(1e9 + 7)
        # dp0[i][j] = arrays with i zeros, j ones, ending with 0
        # dp1[i][j] = arrays with i zeros, j ones, ending with 1
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        # c_pf_1[i][j] = prefix sum of dp1[0...j][i]
        c_pf_1 = [[0]*(zero+1) for _ in range(one+1)]

        # r_pf_0[i][j] = prefix sum of dp0[i][0...j]
        r_pf_0 = [[0]*(one+1) for _ in range(zero+1)]

        # pre-computation for case of 1 zero & one
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1
            r_pf_0[i][0] = 1

        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1
            c_pf_1[j][0] = 1

        for i in range(1, zero+1):
            for j in range(1, one+1):

                # compute dp0[i][j]    
                prev = i - min(i, limit) - 1
                dp0[i][j] = c_pf_1[j][i-1] - (c_pf_1[j][prev] if prev >= 0 else 0)
                dp0[i][j] %= MOD

                r_pf_0[i][j] = dp0[i][j] + (r_pf_0[i][j-1] if j-1 >= 0 else 0)
                
                # compute dp1[i][j]   
                prev = j - min(j, limit) - 1
                dp1[i][j] = r_pf_0[i][j-1] - (r_pf_0[i][prev] if prev >= 0 else 0)
                dp1[i][j] %= MOD

                c_pf_1[j][i] = dp1[i][j] + (c_pf_1[j][i-1] if i-1 >= 0 else 0)

        return (dp0[zero][one] + dp1[zero][one]) % MOD

# constraint
zero, one, limit = 1000, 1000, 1000

Solution().numberOfStableArrays(zero, one, limit)