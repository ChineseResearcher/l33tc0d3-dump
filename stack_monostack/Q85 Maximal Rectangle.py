from typing import List
class Solution:
    def findLargestRec(self, heights: List[int]) -> int:
        # key algorithm for LC84 Largest Rec. in Histogram
        heights.append(0)
        
        st = [-1]
        res = 0
        for i in range(len(heights)):
            
            while heights[i] < heights[st[-1]]:
                h = heights[st.pop()]

                w = i-st[-1]-1
                res = max(res, h*w)
                
            st.append(i)

        return res

    def maximalRectangle(self, matrix: List[List[str]]):
        
        m, n = len(matrix), len(matrix[0])
        # the heights from the top-down perspective can be built from DP
        dp = [0] * n

        fmax = lambda a, b: a if a > b else b
        ans = 0
        # the core idea is to treat this like an extension of LC84 Max. rec. in Histogram
        # we scan through every row, and assume that we are dealing with heights standing on curr. row
        for r in range(m):

            # determine the heights arr.
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[c] += 1
                else:
                    dp[c] = 0

            ans = fmax(ans, self.findLargestRec(dp))

        return ans
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]

Solution().maximalRectangle(matrix)