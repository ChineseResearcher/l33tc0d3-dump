# two pointers - medium
from typing import List
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        m, n = len(boxGrid), len(boxGrid[0])
        final = [ ['.'] * m for _ in range(n) ]

        for r in range(m):

            stone_cnt = 0
            for c in range(n):
                if boxGrid[r][c] == '#':
                    stone_cnt += 1

                elif boxGrid[r][c] == '*':
                    final[c][m-1-r] = '*'
                    for k in range(1, stone_cnt+1):
                        final[c-k][m-1-r] = '#'

                    # reset cnt
                    stone_cnt = 0

            # collect the stone_cnt that fall to the bottom
            for k in range(1, stone_cnt+1):
                final[n-k][m-1-r] = '#'

        return final
    
boxGrid = [["#",".","#"]]
boxGrid = [["#",".","*","."],
           ["#","#","*","."]]
boxGrid = [["#","#","*",".","*","."],
           ["#","#","#","*",".","."],
           ["#","#","#",".","#","."]]

Solution().rotateTheBox(boxGrid)