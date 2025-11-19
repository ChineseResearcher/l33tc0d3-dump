# dp - medium
from typing import List
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:

        n, m = len(source), len(pattern)

        # make targetIndices a set for O(1) membership lookup
        ti = set(targetIndices) 

        # pre-compute a suffix frequency sum of alphabets
        # purpose: for pruning dfs where source[i:] would not be able to generate pattern[j:]
        def sfs(arr):

            sfSum = [ [0] * 26 for _ in range(len(arr)) ]
            for i in range(len(arr)-1, -1, -1):

                curr = ord(arr[i]) - ord('a')
                for char in range(26):
                    prev = 0
                    if i + 1 < len(arr):
                        prev = sfSum[i+1][char]

                    sfSum[i][char] = (1 if char == curr else 0) + prev

            return sfSum

        sf_source, sf_pattern = sfs(source), sfs(pattern) 

        dp = [ [-1] * m for _ in range(n) ]

        def f(i, j):

            # i: index in source; j: index in pattern
            if i == n:
                return float('inf') if j < m else 0
            
            if j == m:
                return 0
            
            # prune based on suffix freq. sum
            curr = ord(pattern[j]) - ord('a')
            if sf_source[i][curr] < sf_pattern[j][curr]:
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]
            
            # no-match
            res = float('inf')
            if source[i] != pattern[j]:
                res = min(res, f(i + 1, j))
            
            else:
                # knapsack dp
                take = (1 if i in ti else 0) + f(i + 1, j + 1)
                skip = f(i + 1, j)
                res = min(res, min(take, skip))

            dp[i][j] = res
            return res

        return len(targetIndices) - f(0, 0)

source, pattern, targetIndices = "abbaa", "aba", [0,1,2]
source, pattern, targetIndices = "bcda", "d", [0,3]
source, pattern, targetIndices = "dda", "dda", [0,1,2]
source, pattern, targetIndices = "yeyeykyded", "yeyyd", [0,2,3,4]
source, pattern, targetIndices = "ordzbihwzbfsukguq", "rdzbugu", [0,2,3,5,6,7,8,9,10,16]

Solution().maxRemovals(source, pattern, targetIndices)