# dp - hard
from typing import Tuple, List
from functools import cache
from collections import defaultdict
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        n = len(board)
        # key ideas:
        # 1) solve top-down DP concerining states (r, c)
        # and return a tuple (k, f), where "x" is the largest sum obtainable
        # with frequency "f"
        # 2) use a hashmap to facilitate results collection at each recursive step

        MOD = int(1e9 + 7)
        @cache
        def f(r:int, c:int) -> Tuple[int]:

            if r == 0 and c == 0:
                return (0, 1)
            
            maxK, v = -1, int(board[r][c]) if board[r][c] != 'S' else 0
            
            res = defaultdict(int)
            for dr, dc in [(0,-1),(-1,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and board[nr][nc] != 'X':
                    k, freq = f(nr, nc)
                    # we only inherit from cells with no dead-end
                    if k != -1:
                        res[v+k] += freq
                        maxK = max(maxK, v+k)

            return (maxK, res[maxK] % MOD)

        k, freq = f(n-1, n-1)
        return [0 if k == -1 else k, freq]
    
board = ["E23","2X2","12S"]
board = ["E12","1X1","21S"]
board = ["E11","XXX","11S"]

Solution().pathsWithMaxScore(board)