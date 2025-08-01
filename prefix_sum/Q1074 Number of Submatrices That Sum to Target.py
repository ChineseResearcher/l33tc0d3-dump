# prefix sum - hard
from typing import List
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
  
        # core idea:
        # 1) build a 2-D prefix sum so that we can compute submatrice area in O(1) time
        # 2) O(n^3) iteration to explore all possible submatrices 
        # by exploring (r1, r2) w/ hashmap-based prefix sum on column index
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

        ans = 0
        for r1 in range(m):
            for r2 in range(r1, m):
                
                # application of hashmap + prefix sum
                # see LC560 Subarray Sum Equal to K
                prefix_dict = defaultdict(int)
                prefix_dict[0] = 1

                curr_sum = 0
                for c in range(n):

                    curr_sum += submatrice_sum(r1, r2, c)
                    ans += prefix_dict[curr_sum - target]

                    prefix_dict[curr_sum] += 1

        return ans
    
matrix, target = [[0,1,0],[1,1,1],[0,1,0]], 0
matrix, target = [[1,-1],[-1,1]], 0
matrix, target = [[1,3,1,3],[3,1,3,1]], 4
matrix, target = [[1,1,1,1],[1,1,1,1],[1,1,0,1],[1,1,1,1]], 4

Solution().numSubmatrixSumTarget(matrix, target)