# sorting - medium
from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        m = len(nums)
        # core ideas:
        # 1) notice that for the i-th diagonal, row + col = i
        # 2) transform input nums to have row + col sum, and sorted by it
        cells = []
        for r in range(m):
            n = len(nums[r])
            for c in range(n):
                cells.append((r+c, r, c))

        cells.sort(key=lambda x:(x[0], -x[1], x[2]))

        ans = []
        for _, r, c in cells:
            ans.append(nums[r][c])

        return ans
    
nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

Solution().findDiagonalOrder(nums)