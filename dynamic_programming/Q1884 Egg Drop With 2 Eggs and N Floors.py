# dp - medium
class Solution:
    def twoEggDrop(self, n: int) -> int:
        # simplified ver. of Q887 w/ only 2 eggs
        dp = [ [0] * (n+1) for _ in range(2) ]

        # when there's only 1 egg, we need n moves to guarantee in worst-case locate 'f'
        for i in range(n+1):
            dp[0][i] = i

        # we directly operate on the second egg level instead of looping it
        egg = 1 # second egg
        for i in range(1, n+1):

            dp[egg][i] = float('inf')
            # exploring all possible predecessor split
            # there's no binary search optimisation needed here as the max. n is just 1000
            # so overall this double-loop is efficient for that input size
            for j in range(i+1):
                
                # do refer to the dfs solution for Q887 to understand this the transitions here
                op1 = dp[egg-1][j-1] + 1
                op2 = dp[egg][i-j] + 1

                if op1 > op2:
                    dp[egg][i] = min(dp[egg][i], op1)
                    
                elif op1 < op2:
                    dp[egg][i] = min(dp[egg][i], op2)

                else:
                    dp[egg][i] = min(dp[egg][i], op1)
                    break

        return dp[1][n]
    
n = 10
# constraints
n = 1000

Solution().twoEggDrop(n)