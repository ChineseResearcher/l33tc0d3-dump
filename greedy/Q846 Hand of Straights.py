# greedy - medium
from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize != 0: return False

        # key ideas:
        # 1) every group has to be size k, and members are consecutive
        # 2) greedily form group by identify the smallest starting member
        # and test if [start, start + 1, start + 2, ..., start + k - 1] are available
        freq = Counter(hand)

        # get our unique numbers and sort in ASC order
        uni = sorted(freq.keys())

        i = 0
        while i < len(uni):

            if freq[uni[i]] == 0:
                i += 1
                continue

            for num in range(uni[i], uni[i] + groupSize):
                if freq[num] == 0:
                    return False

            for num in range(uni[i], uni[i] + groupSize):
                freq[num] -= 1

        return True
    
hand, groupSize = [1,2,3], 1
hand, groupSize = [1,2,3,4,5], 4
hand, groupSize = [1,2,3,6,2,3,4,7,8], 3

Solution().isNStraightHand(hand, groupSize)