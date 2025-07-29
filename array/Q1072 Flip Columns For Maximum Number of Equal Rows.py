# array - medium
from typing import List
class Solution:
    def isInverted(self, s1, s2):
        # for two strings of equal length, 
        # check if they are valid opposition
        n = len(s1)
        for i in range(n):
            if s1[i] == s2[i]:
                return False
        return True

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_pattern = dict()
        m, n = len(matrix), len(matrix[0])

        for row in range(m):

            pattern = []
            for col in range(n):
                pattern.append(str(matrix[row][col]))
            row_pattern[row] = ''.join(pattern)

        # our answer is the maximum colliding count of rows
        # amongst which the 0/1 patterns entirely match OR entirely oppose
        # e.g. 0101 is a valid opposition of 1010
        ans = 1 
        for row in range(m):

            # initiate our baseline pattern to match against
            baseline = row_pattern[row]
            matched = 0
            for row_ in range(m):
                
                curr_pattern = row_pattern[row_]
                if baseline == curr_pattern or self.isInverted(baseline, curr_pattern):
                    matched += 1
                    
                ans = max(ans, matched)

        return ans
    
matrix = [[0,1],[1,1]]
matrix = [[0,1],[1,0]]
matrix = [[0,0,0],[0,0,1],[1,1,0]]

Solution().maxEqualRowsAfterFlips(matrix)