# dp - hard
from functools import cache
class Solution:
    def countWinningSequences(self, s: str) -> int:
        
        n = len(s)
        # pre-define the list of creatures to summon given the prev. round choice
        choice = {'N': ['F', 'W', 'E'], # no choice previously (beginning)
                'F': ['E','W'],
                'E': ['W','F'],
                'W': ['E','F']}

        # pre-define rewards table (2D-dict)
        reward = {'F': {'F':0, 'W':-1, 'E':1},
                'W': {'F':1, 'W':0, 'E':-1},
                'E': {'F':-1, 'W':1, 'E':0}}

        MOD = int(1e9 + 7)
        @cache
        # bob_net records the net points that Bob has over Alice
        def f(i, bob_net, prev):

            if i == n:
                # winning if strictly larger
                return 1 if bob_net > 0 else 0

            # pruning: if bob wins remaining rounds and
            # such that it still loses, early stop
            if bob_net + (n - i) <= 0:
                return 0 
            
            res = 0
            for creature in choice[prev]:
                res += f(i+1, bob_net + reward[creature][s[i]], creature)
                res %= MOD

            return res

        return f(0, 0, 'N')

s = "FFF"
s = "FWEFW"
s = "FWEF" * 250

Solution().countWinningSequences(s)