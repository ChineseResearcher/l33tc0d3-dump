# dp - medium
from typing import List
from functools import cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)
        # key ideas:
        # 1) stone-game equivalent
        # 2) determine curr. player by counting the remaining rounds (i.e. r - l - 1)

        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b

        @cache
        def f(l:int, r:int) -> int:

            if l > r: return 0

            # 0: player1's turn, 1: player2's turn
            currTurn = (n - (r - l + 1)) % 2

            # player1's goal: gain either nums[l] or nums[r] and maximise
            if currTurn == 0:
                return fmax(nums[l] + f(l + 1, r), nums[r] + f(l, r - 1))
            # player2's goal: reduce player1's net gain by either nums[l] or nums[r] and minimise
            else:
                return fmin(-nums[l] + f(l + 1, r), -nums[r] + f(l, r - 1))

        return f(0, n - 1) >= 0 # net gain is non-negative, player1 wins

nums = [1,5,2]
nums = [1,5,233,7]

Solution().predictTheWinner(nums)