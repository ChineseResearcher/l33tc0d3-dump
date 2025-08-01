# binary search - hard
from typing import List
from bisect import insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        # core idea:
        # 1) build a 2-D prefix sum so that we can compute submatrice area in O(1) time
        # 2) O(n^3) iteration to explore all possible submatrices 
        # by exploring (r1, r2) w/ sortedList storing sums of submatrices with rows = [r1...r2]
        # and col = [0...c] for c in range [0, n]
        m, n = len(matrix), len(matrix[0])

        # (1) is natrually a DP problem
        dp = [ [0] * n for _ in range(m) ]

        for r in range(m):
            for c in range(n):

                # area of submatrice w/ bottom right at (r, c)
                # is equal to dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1]
                p1 = dp[r][c-1] if c > 0 else 0
                p2 = dp[r-1][c] if r > 0 else 0
                p3 = dp[r-1][c-1] if r > 0 and c > 0 else 0

                dp[r][c] = p1 + p2 - p3 + matrix[r][c]

        def submatrice_sum(r1, r2, c):

            if r1 == r2:
                return matrix[r1][c]
            
            a1 = dp[r2][c]
            a2 = dp[r2][c-1] if c-1 >= 0 else 0
            a3 = dp[r1-1][c] if r1-1 >= 0 else 0
            a4 = dp[r1-1][c-1] if r1-1 >= 0 and c-1 >= 0 else 0

            return a1 - a2 - a3 + a4

        ans = float('-inf')
        for r1 in range(m):
            for r2 in range(r1, m):
                
                curr_sum, sl = 0, [0]
                for c in range(n):

                    curr_sum += submatrice_sum(r1, r2, c)
                    # bs on sorted list
                    l, r = 0, len(sl)-1
                    while l <= r:

                        mid = (l + r) // 2
                        if curr_sum - sl[mid] <= k:
                            ans = max(ans, curr_sum - sl[mid])
                            r = mid - 1
                        else:
                            l = mid + 1

                    insort(sl, curr_sum)

        return ans
    
matrix, k = [[1,0,1],[0,-2,3]], 2
matrix, k = [[2,2,-1]], 3
matrix, k = [[2,2,-1]], 0

Solution().maxSumSubmatrix(matrix, k)