# dp - hard
from typing import List
from functools import cache
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        n = len(fruits)
        # core ideas:
        # 1) player starting at (0,0) will always have to take the diagonal path

        # 2) player starting at (n-1,0) will always have to move in the lower halve under
        # the diagonal of the square, technically he / she can touch the diagonal but it's
        # meaningless because it would be collected by player starting at (0,0) anyways

        # 3) similarly, player starting at (0,n-1) will always have to move in the
        # upper halve above the diagonal of the square

        # solver for (2)
        @cache
        def solve1(r, c):

            if r == n-1 and c == n-1:
                return 0
            
            # player starting at (n-1,0) can move in three directions
            delta = [(1,1), (0,1), (-1,1)]

            curr_res = 0
            for dx, dy in delta:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) == (n-1, n-1) or nr > nc:
                        curr_res = max(curr_res, fruits[r][c] + solve1(nr, nc))

            return curr_res

        p1 = solve1(n-1, 0)

        # solver for (3)
        @cache
        def solve2(r, c):

            if r == n-1 and c == n-1:
                return 0
            
            # player starting at (n-1,0) can move in three directions
            delta = [(1,-1), (1,0), (1,1)]

            curr_res = 0
            for dx, dy in delta:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) == (n-1, n-1) or nc > nr:
                        curr_res = max(curr_res, fruits[r][c] + solve2(nr, nc))

            return curr_res

        p2 = solve2(0, n-1)

        # then add up all the diagonal values
        ans = p1 + p2
        for i in range(n):
            ans += fruits[i][i]

        return ans
    
fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
fruits = [[1,1],[1,1]]

Solution().maxCollectedFruits(fruits)