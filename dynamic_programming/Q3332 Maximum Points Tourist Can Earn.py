# dp - medium
from typing import List
from functools import cache
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def recursive_tour(day, city):

            if day == k:
                return 0
            
            curr_res = 0
            # stay in curr. city for the day
            curr_res = max(curr_res, stayScore[day][city] + recursive_tour(day+1, city))

            # every city is connected every other city
            # in total there are n cities
            for neighbour in range(n):

                # travel to that city
                curr_res = max(curr_res, travelScore[city][neighbour] + \
                                        recursive_tour(day + 1, neighbour))
                
            return curr_res

        ans = 0
        # init. diff. cities as the starting point
        for i in range(n):
            ans = max(ans, recursive_tour(0, i))

        return ans
    
n, k, stayScore, travelScore = 2, 1, [[2,3]], [[0,2],[1,0]]
n, k, stayScore, travelScore = 3, 2, [[3,4,2],[2,1,2]], [[0,2,1],[2,0,4],[3,2,0]]

Solution().maxScore(n, k, stayScore, travelScore)