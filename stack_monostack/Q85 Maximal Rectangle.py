from collections import defaultdict
class Solution:
    def prevSmaller(self, subarr):
        n = len(subarr)
        smaller = [-1] * n

        stack = []
        for i, num in enumerate(subarr):

            if not stack:
                stack.append(i)
                continue

            if num > subarr[stack[-1]]:
                smaller[i] = stack[-1]
                continue

            # if it's 0, we append its idx
            stack.append(i)

        return smaller

    def findLargestRec(self, heights):
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

    def maximalRectangle(self, matrix):
        
        m, n = len(matrix), len(matrix[0])
        # for a specific col, store the prev. '0' cell row pos
        # given a '1' cell in the same col
        col_wise_smaller = defaultdict(list)

        # precompute for col
        for c in range(n):
            subarr = [matrix[r][c] for r in range(m)]
            col_wise_smaller[c] = self.prevSmaller(subarr)

        ans = 0
        # the core idea is to treat this like an extension of LC84 Max. rec. in Histogram
        # we scan through every row, and assume that we are dealing with heights standing on curr. row
        for r in range(m-1, -1, -1):

            # determine the heights arr. if we are to 
            # base our heights at row r
            heights = [r-col_wise_smaller[c][r] if matrix[r][c] == '1' else 0 for c in range(n)]
            ans = max(ans, self.findLargestRec(heights))

        return ans
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]

Solution().maximalRectangle(matrix)