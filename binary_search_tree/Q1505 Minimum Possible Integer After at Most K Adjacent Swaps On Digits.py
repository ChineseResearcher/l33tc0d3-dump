# bst - hard
from sortedcontainers import SortedList
from collections import deque
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        
        n = len(num)
        # the general idea is for every round, always bring the
        # smallest possible integer to the front, subject to k swaps available

        # store the digits' indices in its respective deque
        digits = {i:deque([]) for i in '0123456789'}
        for idx, digit in enumerate(num):
            digits[digit].append(idx)
            
        # one of the tricky thing is as we swap, indices of digits change
        # so the number of swaps to bring a digit to the front is also not fixed
        # we need an efficient way of knowing exactly this number for the curr. rnd
        pickedIdx = SortedList([])

        # maintain a stack to store all digits brought to the front
        swapped = []

        while True:
            
            # mark a boolean to indicate if we found any digit can
            # be brought forward for this round
            canShift = False
            
            # there's a greedy thinking applied here as we always
            # want the smallest possible digit to be brought forward
            for d in '0123456789':
                if digits[d] and digits[d][0] - pickedIdx.bisect_left(digits[d][0]) <= k:
                    canShift = True
                    break
                    
            if not canShift:
                break
            
            # reference the "d" above
            currDigit, currIdx = d, digits[d].popleft()
            k -= currIdx - pickedIdx.bisect_left(currIdx)
            # add this digit to swapped section
            swapped.append(currDigit)
            
            # add current index as an picked index to our PBDS
            pickedIdx.add(currIdx)
            
        # unpack the unswapped from digits and sort by indices instead
        temp = []
        for d in digits.keys():
            for idx in digits[d]:
                temp.append([idx, d])
            
        temp.sort()
        unswapped = [x[1] for x in temp]

        return ''.join(swapped) + ''.join(unswapped)
    
num, k = "4321", 4
num, k = "100", 1
num, k = "36789", 1000
num, k = "294984148179", 11

Solution().minInteger(num, k)