# graph - medium
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        # idea of the game is:
        # 1) we start at cell 1, to win, need to reach cell n^2
        # 2) at each cell, roll the dice to move 1-6 steps forward if possible
        # 3) w/ ladder, we go to larger cell, w/ snake we (might) regress to a smaller cell
        n = len(board)

        # determine the forwardFill status for each row
        ff, status = dict(), True
        for r in range(n-1, -1, -1):
            ff[r] = status
            status = not status

        # it's better to build a mapping from number to (r,c) and vice versa
        # cellMap: given a cell number, access the (r,c) coordinate
        # rcMap: given a coordinate, access the cell number
        cellMap, rcMap = dict(), dict()
        for cellVal in range(1, n ** 2 + 1):

            r = n - 1 - ((cellVal - 1) // n)
            # because of the style that matrix values are filled,
            # we have to alternate in the direction of filling
            c = (cellVal - 1) % n if ff[r] else n - 1 - ((cellVal - 1) % n)
            # mapping
            cellMap[cellVal] = (r,c)
            rcMap[(r,c)] = cellVal

        # we enque the unique cell values instead of coordinates
        # at the same time tracking the number of moves
        # note: it's guaranteeed that starting position does NOT have ladder or snake
        q, visited = deque([(1, 0)]), set([1])
        while q:

            val, dist = q.popleft()
            if val == n ** 2:
                return dist

            # dice-roll
            for dr in range(val+1, min(val+6, n ** 2) + 1):

                nr, nc = cellMap[dr]
                if board[nr][nc] == -1:
                    next_val = dr
                else:
                    next_val = board[nr][nc]

                if next_val not in visited:
                    q.append((next_val, dist+1))
                    visited.add(next_val)

        return -1
    
board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [10,15,-1,-1,-1,-1]]

board = [[-1,-1],
         [-1,3]]

board = [[-1,1,2,-1],
         [2,13,15,-1],
         [-1,10,-1,-1],
         [-1,6,2,8]]

board = [[1,1,-1],
         [1,1,1],
         [-1,1,1]]

Solution().snakesAndLadders(board)