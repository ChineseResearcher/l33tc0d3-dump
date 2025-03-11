# dp - medium
class Solution:
    def maxScore(self, a, b):
        # n is always of length 4
        m, n = len(b), len(a)
        # this question is a classical knapsack problem variation
        dp = [ [0] * (n+1) for _ in range(m+1) ]

        # since multiplication can lead to negative numbers
        # our first row/col dp vals are init. to float('-inf)
        for i in range(n+1):
            dp[0][i] = float('-inf')
        for i in range(m+1):
            dp[i][0] = float('-inf')

        # traverse the transition states in O(4*m) time
        for i in range(1, m+1):
            for j in range(1, n+1):

                # a problem become undefined when we have fewer b elements
                # then the number of a elements we can choose
                if j > i:
                    dp[i][j] = dp[i-1][j]
                else:
                    # first option is to skip the curr. 'b' element
                    skip = dp[i-1][j]

                    # second option is to consider the curr. 'b' element
                    take = b[i-1] * a[j-1] + (dp[i-1][j-1] if dp[i-1][j-1] > float('-inf') else 0)

                    dp[i][j] = max(skip, take)

        return dp[-1][-1]
    
a, b = [3,2,5,6], [2,-6,4,-5,-3,2,-7]
a, b = [-1,4,5,-2], [-5,-1,-3,-2,-4]

Solution().maxScore(a, b)