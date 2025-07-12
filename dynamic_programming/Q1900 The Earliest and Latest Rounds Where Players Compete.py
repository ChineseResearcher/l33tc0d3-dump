# dp - hard
from functools import cache
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        @cache
        def recursive_play(l, r, m):
            '''
            l: the (1-based) index of the first player starting from left
            r: the (1-based) index of the second player starting from right
            m: total number of players this round

            e.g. [1,2,3,4,5] where 1, 4 are the two dominant players
            then l = 1, r = 2, m = 5
            '''

            # if the two dominant players are in symmetric pos.
            # we have come to the end of the simulation
            if l == r:
                return 1
            
            curr_res = float('inf') if findEarliest else 0
            # realise that we do not care whether l refers to the
            # index of the "first player" or whether r refer to the index
            # of the "second player" strictly, hence the problem can be 
            # always converted to make sure l < r
            if l > r:
                curr_res = recursive_play(r, l, m)
            else:

                # we are simulating how many players including and before l
                # are winning this round, and thus giving a bound to
                # how many players can win including and after r
                # note: because we made sure l < r, the range [l-i+1, r-i+1] would then be valid
                for i in range(1, l+1):
                    for j in range(l-i+1, r-i+1):

                        # (i, j) would just mean for the next rnd
                        # l = i, r = j, plus potentially some players in between

                        # (1) i + j cannot exceed the total players next round
                        if i + j > (m + 1) // 2:
                            continue

                        # (2) i + j cannot be smaller than the worst case scenario
                        # where m // 2 players who lost all came from [1...l] and [j...m]
                        if i + j < l + r - m // 2:
                            continue
                        
                        next_res = 1 + recursive_play(i, j, (m + 1) // 2)
                        curr_res = min(curr_res, next_res) if findEarliest else max(curr_res, next_res)

            return curr_res

        ans = []

        findEarliest = True
        ans.append(recursive_play(firstPlayer, n - secondPlayer + 1, n))

        recursive_play.cache_clear()

        findEarliest = False
        ans.append(recursive_play(firstPlayer, n - secondPlayer + 1, n))

        return ans
    
n, firstPlayer, secondPlayer = 11, 2, 4
n, firstPlayer, secondPlayer = 5, 1, 5
n, firstPlayer, secondPlayer = 28, 10, 20 # constraint
n, firstPlayer, secondPlayer = 5, 1, 4
n, firstPlayer, secondPlayer = 10, 1, 8

Solution().earliestAndLatest(n, firstPlayer, secondPlayer)