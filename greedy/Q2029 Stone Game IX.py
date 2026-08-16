# greedy - medium
from typing import List
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        n = len(stones)
        if n == 1: return False
        # key ideas:
        # 1) the playoff sequence can be deterministic after Alice's first move
        # 2) suppose we take mod3 over all stones, and there are no stones with mod3 = 0,
        # if Alice picks 1 (mod3 = 1) as the 1st, sequence will have to be [(1),1,2,1,2,...]
        # and whoever runs out of their corresponding 1 / 2 choices first or consumes last stone will lose
        # 3) if there are stones w/ mod3 = 0, then it simply reverses the stones to be taken 
        # between Alice and Bob. For example, suppose Alice starts w/ 1, the sequence looks like
        # following if 0 is chosen somewhere by either player [(1),1,2,0,1,2,...]

        # process for mod3 results
        stoneMOD3 = {0:0, 1:0, 2:0}
        for x in stones:
            stoneMOD3[x % 3] += 1

        if stoneMOD3[1] == stoneMOD3[2] == 0: return False

        # simulate helper
        def simulate(alice_first_pick:int, freq:dict) -> bool:
            # init. the simulation config.
            if alice_first_pick == 1:
                alice, bob = 2, 1
                freq[1] -= 1
            elif alice_first_pick == 2:
                alice, bob = 1, 2
                freq[2] -= 1

            AliceWin = True
            for round in range(n - 1):
                # Bob's turn
                if round % 2 == 0:
                    if freq[bob] > 0:
                        freq[bob] -= 1
                    else:
                        if freq[0] == 0:
                            break
                        freq[0] -= 1
                        alice, bob = bob, alice

                # Alice's turn
                else:
                    if freq[alice] > 0:
                        freq[alice] -= 1
                    else:
                        if freq[0] == 0:
                            AliceWin = False
                            break
                        freq[0] -= 1
                        alice, bob = bob, alice

                # additional check on last stone taken:
                # if reached, alice must have lost because the simulation
                # ensures taken sum so far is not divisbile by 3 at any point
                if round == n - 2:
                    AliceWin = False

            return AliceWin

        op1 = simulate(1, stoneMOD3.copy()) if stoneMOD3[1] > 0 else False
        op2 = simulate(2, stoneMOD3.copy()) if stoneMOD3[2] > 0 else False

        return op1 or op2

stones = [2]
stones = [2,1]
stones = [5,1,2,4,3]

Solution().stoneGameIX(stones)