# dp - medium
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        MOD = int(1e9 + 7)
        # dp0[i][j] = arrays with i zeros, j ones, ending with 0
        # dp1[i][j] = arrays with i zeros, j ones, ending with 1
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                if i == 0 and j == 0:
                    continue
                
                # compute dp0[i][j]
                if i > 0:
                    total = 0
                    for k in range(1, limit+1):
                        if k > i:
                            break
                        total += dp1[i-k][j]
                    dp0[i][j] += total % MOD
                
                # compute dp1[i][j]
                if j > 0:
                    total = 0
                    for k in range(1, limit+1):
                        if k > j:
                            break
                        total += dp0[i][j-k]
                    dp1[i][j] += total % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD

zero, one, limit = 1, 1, 2
zero, one, limit = 1, 2, 1
zero, one, limit = 3, 3, 2
zero, one, limit = 1, 3, 1
zero, one, limit = 1, 4, 2
zero, one, limit = 1, 4, 1
zero, one, limit = 2, 4, 2
zero, one, limit = 1, 5, 2
zero, one, limit = 19, 15, 15
zero, one, limit = 64, 59, 47
zero, one, limit = 198, 199, 197

Solution().numberOfStableArrays(zero, one, limit)