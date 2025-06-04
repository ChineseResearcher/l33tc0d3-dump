# dp - hard
from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        def recursive_jump(currIdx):

            if dp[currIdx] != -1:
                return dp[currIdx]

            curr_ans = 1
            next_best = 0
            # forward jump
            for i in range(currIdx+1, min(currIdx+d+1, n)):
                if arr[i] >= arr[currIdx]:
                    break
                next_best = max(next_best, recursive_jump(i))

            # backward jump
            for j in range(currIdx-1, max(currIdx-d-1, -1), -1):
                if arr[j] >= arr[currIdx]:
                    break
                next_best = max(next_best, recursive_jump(j))

            dp[currIdx] = curr_ans + next_best
            return curr_ans + next_best

        dp = [-1] * n
        for startPos in range(n):

            if dp[startPos] == -1:
                _ = recursive_jump(startPos)

        return max(dp)
    
arr, d = [6,4,14,6,8,13,9,7,10,6,12], 2
arr, d = [3,3,3,3,3], 3
arr, d = [7,6,5,4,3,2,1], 1

Solution().maxJumps(arr, d)