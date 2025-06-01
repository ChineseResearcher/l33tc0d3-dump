# greedy - hard
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # we have to distribute at least one candy to each child
        dist = [1] * n

        for i in range(1, n):

            if ratings[i] > ratings[i-1]:
                dist[i] = max(dist[i], dist[i-1] + 1)

        for j in range(n-2, -1, -1):

            if ratings[j] > ratings[j+1]:
                dist[j] = max(dist[j], dist[j+1] + 1)

        return sum(dist)
    
ratings = [1,0,2]
ratings = [1,2,3,8,7,6,6,5,4,3]
ratings = [1,3,2,2,1]

Solution().candy(ratings)