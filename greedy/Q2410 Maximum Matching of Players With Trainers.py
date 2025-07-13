# greedy - medium
from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        m, n = len(players), len(trainers)
        j = 0 # pointer for trainers

        ans = 0
        for i in range(m):

            while j < n and trainers[j] < players[i]:
                j += 1

            if j == n:
                break

            ans += 1 # matched
            j += 1

        return ans
    
players, trainers = [4,7,9], [8,2,5,8]
players, trainers = [1,1,1], [10]

Solution().matchPlayersAndTrainers(players, trainers)