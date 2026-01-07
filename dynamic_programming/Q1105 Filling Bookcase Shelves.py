# dp - medium
from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)
        width = [0] + [x[0] for x in books]
        height = [0] + [x[1] for x in books]

        # dp[i] stores the solution to the subproblem concerning books[:i]
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            thickness_sum, max_height, curr_height = 0, 0, float('inf')
            for j in range(i, 0, -1):
                
                thickness_sum += width[j]
                if thickness_sum > shelfWidth:
                    break
                
                # the challenging part is in making use of the thickness condition check
                # to point to the valid last_height for us to compare and compute the curr_height
                max_height = max(max_height, height[j])
                last_height = dp[j-1]
                curr_height = min(curr_height, max_height + last_height)
                
            dp[i] = curr_height

        return dp[-1]
    
books, shelfWidth = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4
books, shelfWidth = [[1,3],[2,4],[3,2]], 6

Solution().minHeightShelves(books, shelfWidth)