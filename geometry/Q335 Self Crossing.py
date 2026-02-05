# geometry - hard
from typing import List
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:

        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) there can only be self-crossing if the path starts to involute
        # i.e. at some point (either x- or y-axis) movement is smaller or equal to
        # prior x-/y-axis movement correspondingly

        # 2) using the above logic to detect the start of involution, and 
        # report self-crossing when curr. movement touches some lines

        # 3) determining the search space can be tricky, and through observation we could
        # reduce our search space to the (up to) the last 5 lines before the curr. line

        # 4) we then need to store our horizontal / vertical lines

        involuted = False
        prev_delta = [float('inf'),float('inf')] # <y, x>
        prev_lines = [ [] for _ in range(2) ]

        # signs for delta
        s = [1,-1,-1,1]

        selfCrossing, coord = False, [0,0]
        for idx, delta in enumerate(distance):

            n_coord = coord[:]
            imod2, imod4 = idx % 2, idx % 4
            n_coord[1 - imod2] += s[imod4] * delta

            # check for selfCrossing when involution has started
            if involuted:
        
                # check w/ 3rd and 5th last line
                for length in [2, 3]:
                    if len(prev_lines[1-imod2]) >= length:
                        pl = prev_lines[1-imod2][-length]
                        diff = pl[0] - coord[1-imod2]
                        # check for valid direction and range
                        if diff * s[imod4] > 0 and pl[1] <= coord[imod2] <= pl[2]:
                            if delta >= abs(diff):
                                selfCrossing = True
                                break
                
                # check w/ 4th last line
                if len(prev_lines[imod2]) >= 2:
                    pl = prev_lines[imod2][-2]
                    if n_coord[imod2] == pl[0]:
                        # check for valid range
                        if pl[1] <= n_coord[1-imod2] <= pl[2]:
                            selfCrossing = True
                            break
            
            # update involuted status & prev_delta
            if idx > 1:
                involuted |= (delta <= prev_delta[imod2])
            prev_delta[imod2] = delta

            # store curr. line
            if imod2 == 0:
                l = (n_coord[0], fmin(coord[1], n_coord[1]), fmax(coord[1], n_coord[1]))
            else:
                l = (n_coord[1], fmin(coord[0], n_coord[0]), fmax(coord[0], n_coord[0]))
            prev_lines[imod2].append(l)

            # update coord
            coord = n_coord

        return selfCrossing

distance = [2,1,1,2]
distance = [1,2,3,4]
distance = [1,1,1,2,1]
distance = [2,1,1,1]
distance = [2,1,3,2,2,1]
distance = [1,1,2,2,3,1,1]
distance = [1,1,2,1,1]
distance = [3,3,3,2,1,1]
distance = [1,1,3,2,1,1]

Solution().isSelfCrossing(distance)