# dp - medium
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        dp = [None] * (n+1)
        # dummy day takes costs 0
        dp[0] = 0

        for i in range(1, n+1):

            curr_ans = float('inf')
            for j in range(i-1, -1, -1):
                
                # exceed max. coverage of 30 days
                if days[i-1] - days[j] + 1 > 30:
                    break
                
                # 1-day ticket
                if days[i-1] - days[j] + 1 <= 1:
                    curr_ans = min(curr_ans, dp[j] + costs[0])
                
                # 7-day ticket
                if days[i-1] - days[j] + 1 <= 7:
                    curr_ans = min(curr_ans, dp[j] + costs[1])

                # 30-day ticket
                if days[i-1] - days[j] + 1 <= 30:
                    curr_ans = min(curr_ans, dp[j] + costs[2])

            dp[i] = curr_ans

        return dp[-1]  
    
days, costs = [1,4,6,7,8,20], [2,7,15]
days, costs = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]
days, costs = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]     

Solution().mincostTickets(days, costs)