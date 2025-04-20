# greedy - medium
from collections import Counter
class Solution:
    def numRabbits(self, answers):
        
        # note the the total number of rabbits is strictly unknown
        # so the n answers we collected is just a subset of the population
        n = len(answers)

        # tabulate the freq. of each answer
        freq = Counter(answers)

        minCnt = 0
        for k, v in freq.items():

            # if answer is 0, the person has to be
            # a group on its own (no other rabbits have same color)
            if k == 0:
                minCnt += v

            else:
                # for non-zero answer, the implied group size is
                # k + 1, and the greedy way to achieving min. cnt
                # is to always assume the those who are interviewed
                # and gave the same answer are in the same grp.
                grpSize = k + 1
                minCnt += (v // grpSize) * grpSize

                # any leftover occurrences refer to another grp
                v -= (v // grpSize) * grpSize
                if v > 0:
                    minCnt += grpSize

        return minCnt
    
answers = [1,1,2]
answers = [10,10,10]
answers = [0,0,1,1,1]
answers = [24,24,24,24,2,2,1,2,8,8,2,8,8]

Solution().numRabbits(answers)