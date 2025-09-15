# dp - hard
from functools import cache
from collections import Counter
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        def collapse(board:str) -> str:

            st = []
            for char in board:
                if len(st) >= 3 and char != st[-1] and st[-1] == st[-2] == st[-3]:
                    to_pop = st[-1]
                    while st and st[-1] == to_pop:
                        st.pop()

                st.append(char)

            if len(st) >= 3 and st[-1] == st[-2] == st[-3]:
                to_pop = st[-1]
                while st and st[-1] == to_pop:
                    st.pop()

            if not st:
                return ''
            
            return ''.join(st)

        # encode freq. of colors: RYBGW
        cf = Counter(hand)
        hand = ''.join([str(cf[c]) for c in "RYBGW"])

        @cache
        def recursive_game(board, usedHand):

            if board == '':
                return 0
            
            res, n = float('inf'), len(board)
            for idx, char in enumerate('RYBGW'):
                # find unused hand
                f = int(usedHand[idx])
                if f > 0:

                    new_hand = usedHand[:idx] + str(f-1) + usedHand[idx+1:]

                    # try diff. insert pos.
                    for j in range(n):
                        
                        # meaningful insertion?
                        # 1) e.g. insert 'B' when board[j] is 'B'
                        # 2) e.g. insert 'B' (or any char) in between when we have 'RR', 'YY', 'BB', ...
                        if char == board[j] or (j < n-1 and board[j] == board[j+1]):
                            # we need to cancel out all consecutive groups as they arise
                            new_board = collapse(board[:j+1] + char + board[j+1:])
                            res = min(res, 1 + recursive_game(new_board, new_hand))

            return res

        res = recursive_game(board, hand)
        return res if res < float('inf') else -1
    
board, hand = "WRRBBW", "RB"
board, hand = "WWRRBBWW", "WRBRW"
board, hand = "G", "GGGGG"
board, hand = "RRWWRRBBRR", "WB"
board, hand = "WWBBWBBWW", "BB"
board, hand = "RRYGGYYRRYYGGYRR", "GGBBB"
board, hand = "RRGGBBYYWWRRGGBB", "RGBYW"

Solution().findMinStep(board, hand)