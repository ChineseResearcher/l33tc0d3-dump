# two pointers - medium
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # handle edge case: only one type of status
        if len(set(dominoes)) == 1:
            return dominoes

        currR, currL, final = -1, -1, []

        for idx, state in enumerate(dominoes):

            if state == 'R':
                if currR > currL:
                    final.extend(["R"] * (idx-currR-1))
                else:
                    final.extend(["."] * (idx-currL-1))
                final.append(state)
                currR = idx

            elif state == 'L':

                if currL >= currR:
                    # dots in between all turn to L
                    final.extend(["L"] * (idx-currL-1))

                else:
                    # dots in between all to L/R 
                    # formualtion depends on the count of dots being odd or even

                    if (idx-currR-1) % 2 == 0: # even case
                        final.extend(["R"] * ((idx-currR-1)//2) + ["L"] * ((idx-currR-1)//2))
                    else: # odd case
                        final.extend(["R"] * ((idx-currR-1)//2) + ["."] + ["L"] * ((idx-currR-1)//2))
                        
                final.append(state)
                currL = idx

        if dominoes[-1] == ".":

            if currR > currL:
                final.extend(["R"] * (idx-currR))
            elif currR < currL:
                final.extend(["."] * (idx-currL))

        return ''.join(final)
    
dominoes = "."
dominoes = "RR.L"
dominoes = ".L.R...LR..L.."

Solution().pushDominoes(dominoes)