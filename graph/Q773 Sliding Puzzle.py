# graph - hard
from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        # dfs w/ memo won't work because we could be stuck in
        # infinite dfs chain when we move in circular fashion

        # use bfs and explore the potential transformations
        # which have not been VISITED

        # let board[0][0],..., board[0][2], board[1][0],..., board[1][2]
        # be represented as [0...5] on flattened 1-d indices
        # then encode the possible swapping for each indice
        swaps = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        def str_swap(s, i, j):

            if j < i:
                i, j = j, i

            # helper to swap string chars at (i, j)
            return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

        board_vals = []
        for r in board:
            for x in r:
                board_vals.append(str(x))

        start = ''.join(board_vals)

        visited = set([start])
        q = deque(((start, start.index('0'), 0),))

        while q:

            curr_board, zero_pos, steps = q.popleft()
            if curr_board == '123450':
                return steps
            
            for next_pos in swaps[zero_pos]:
                next_board = str_swap(curr_board, next_pos, zero_pos)

                if next_board not in visited:
                    q.append((next_board, next_pos, steps+1))
                    visited.add(next_board)

        return -1 # no soln
    
board = [[1,2,3],[4,0,5]]
board = [[1,2,3],[5,4,0]]
board = [[4,1,2],[5,0,3]]

Solution().slidingPuzzle(board)