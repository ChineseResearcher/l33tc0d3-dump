# simulation - medium
class Solution:
    def equalPairs(self, grid) -> int:
        row_dict = dict()
        col_dict = dict()

        n = len(grid)
        for i in range(n):
            col_dict[i] = [grid[j][i] for j in range(n)]
            row_dict[i] = grid[i]

        ans = 0 # our row-col match pairs
        for i in range(n):
            row = row_dict[i]
            for j in range(n):
                if col_dict[j] == row:
                    ans += 1

        return ans
    
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

Solution().equalPairs(grid)