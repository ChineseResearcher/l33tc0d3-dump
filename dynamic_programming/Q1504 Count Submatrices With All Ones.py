# dp - medium
from typing import List
# O(n^3) ver. w/ no DP / monotonic stack
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # first build a 2-D array h, 
        # where h[r][c] denotes the height rooted at mat[r][c] vertically
        h = [ [0] * n for _ in range(m) ]
        for c in range(n):

            currH = 0
            for r in range(m):
                if mat[r][c] == 0:
                    currH = 0
                else:
                    currH += 1

                h[r][c] = currH

        ans = 0
        for r in range(m):

            # for every row, we retrive the heights rooted at this level
            h_arr = h[r]
            for c in range(n):
                if h_arr[c] == 0:
                    continue
                
                # bounding height
                bh = h_arr[c]
                for k in range(c, -1, -1):
                    if h_arr[k] == 0:
                        break
                    
                    bh = min(bh, h_arr[k])
                    ans += bh
            
        return ans

# improved O(n^2) ver.
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        # first build a 2-D array h, 
        # where h[r][c] denotes the height rooted at mat[r][c] vertically
        h = [ [0] * n for _ in range(m) ]
        for c in range(n):

            currH = 0
            for r in range(m):
                if mat[r][c] == 0:
                    currH = 0
                else:
                    currH += 1

                h[r][c] = currH

        def findsmaller(arr):

            # helper to find the first equal or smaller element
            # to the left for every arr[i], using monotonic stack

            n = len(arr)

            leftSmaller, monoStack = [-1] * n, []
            for i in range(n-1, -1, -1):

                while monoStack and arr[i] <= arr[monoStack[-1]]:
                    leftSmaller[monoStack.pop()] = i

                monoStack.append(i)

            return leftSmaller

        # build a 2-D dp arr. where dp[i][j] stores the no. of
        # all 1-submatrices w/ bottom right at (i, j)
        dp = [ [0] * n for _ in range(m) ]

        ans = 0
        for r in range(m):

            # for every row, we retrive the heights rooted at this level
            h_arr = h[r]
            # compute the leftSmaller positions
            lm = findsmaller(h_arr)

            # we rely on this lm arr. for inheritance
            for c in range(n):

                p = lm[c]

                # if there are some col "p", where p < c and the height
                # rooted at p is smaller or equal to height at c and non-zero, then
                # we inherit the dp result at dp[r][p]
                dp[r][c] += dp[r][p]

                # for the curr col "c", we increment h_arr[c] to the dp result
                # because a height of x rooted at mat[r][c] would mean we have
                # x all-1 submatrices to be recognised, w/ (r,c) as the bottom right
                dp[r][c] += h_arr[c] * (c-p)
                    
                ans += dp[r][c]

        return ans
    
mat = [[1,0,1],[1,1,0],[1,1,0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
mat = [[1,0,0,1,0,1,0,1],[1,0,1,1,0,1,0,0],[1,1,1,0,1,0,0,1],
       [0,0,1,1,1,1,0,0],[0,0,1,1,1,1,0,1],[1,1,0,1,1,1,0,0]]

Solution().numSubmat(mat)