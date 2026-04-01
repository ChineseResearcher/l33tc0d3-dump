# stack - hard
from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        n = len(positions)
        # key ideas:
        # 1) first sort directions based on positions
        # 2) use a stack to simulate any collisions
        # 3) make ongoing updates to "healths" as any "R" in stack encounters a new "L"
        t = [(x, i) for i, x in enumerate(positions)]
        t.sort()

        d = []
        for _, i in t:
            d.append((directions[i], i))

        st = []
        for dir, i in d:

            if dir == 'R':
                st.append(i)
                continue
            
            # for an incoming "L", simulate collisions if any
            survived = True
            while st and directions[st[-1]] == 'R':
                # incoming is stronger
                if healths[i] > healths[st[-1]]:
                    healths[i] -= 1
                    healths[st[-1]] = -1 # mark dead
                    st.pop()

                # incoming is weaker
                elif healths[i] < healths[st[-1]]:
                    healths[st[-1]] -= 1
                    healths[i] = -1
                    survived = False
                    break

                # same strength
                else:
                    healths[i] = -1
                    healths[st[-1]] = -1
                    st.pop()
                    survived = False
                    break

            if survived:
                st.append(i)

        return [healths[i] for i in range(n) if healths[i] != -1]

positions, healths, directions = [1,40], [10,11], "RL"
positions, healths, directions = [13,3], [17,2], "LR"
positions, healths, directions = [5,4,3,2,1], [2,17,9,15,10], "RRRRR"
positions, healths, directions = [3,5,2,6], [10,10,15,12], "RLRL"
positions, healths, directions = [1,2,5,6], [10,10,11,11], "RLRL"

Solution().survivedRobotsHealths(positions, healths, directions)