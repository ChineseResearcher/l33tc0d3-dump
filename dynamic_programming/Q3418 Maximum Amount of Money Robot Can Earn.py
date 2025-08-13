# dp - medium
from typing import List
from functools import cache
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        m, n = len(coins), len(coins[0])
        # core ideas:
        # 1) classic matrix DP w/ top-down search from start to destination
        # 2) keep track of wildcard left in the states

        @cache
        def recursive_play(r, c, wildcard):
            
            if r == m-1 and c == n-1:
                if coins[r][c] < 0:
                    return 0 if wildcard > 0 else coins[r][c]
                else:
                    return coins[r][c]
                
            curr_res, val = float('-inf'), coins[r][c]
            # take the reward / damage by robber and go right
            if c + 1 < n:
                curr_res = max(curr_res, val + recursive_play(r, c+1, wildcard))
                if val < 0 and wildcard > 0:
                    # avoid the damage and go right
                    curr_res = max(curr_res, recursive_play(r, c+1, wildcard-1))

            # take the reward / damage and go down
            if r + 1 < m:
                curr_res = max(curr_res, val + recursive_play(r+1, c, wildcard))
                if val < 0 and wildcard > 0:
                    # avoid the damage and go down
                    curr_res = max(curr_res, recursive_play(r+1, c, wildcard-1))

            return curr_res
        
        return recursive_play(0, 0, 2)
    
coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
coins = [[10,10,10],[10,10,10]]

Solution().maximumAmount(coins)