# greedy - hard
from typing import List
from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
        c1, c2 = Counter(basket1), Counter(basket2)
        # first determine if there are any items whose total cnt is odd
        # this would immediately tell us it's impossible to distribute evenly
        for k in (c1.keys() | c2.keys()):
            if (c1[k] + c2[k]) % 2 != 0:
                return - 1

        # create two stacks to store the items which have extra occurrences in each basket
        s1 = [k for k in c1.keys() if c1[k] > c2[k]]
        s2 = [k for k in c2.keys() if c2[k] > c1[k]]

        if not s1 and not s2:
            return 0

        # greedy at work, why sort in opposite manners?
        # key idea 1: we do not want the cheaper pairs to go together
        # and by sorting in opposite directions instead, we ensure the pairing is greedily
        # the most cost-efficient as there's always the i-th cheapest item from one of the stacks
        s1.sort()
        s2.sort(reverse=True)

        # let whichever having the smaller end be in the reverse state
        if s1[0] < s2[-1]:
            s1 = s1[::-1]
            s2 = s2[::-1]

        # key idea 2: swapping need not always be direct exchange
        # it can be using an already equal-in-count common item to perform an indirect exchange
        # first find the smallest price of such an item
        best_min = float('inf')
        # a common item would be in both s1 & s2
        for x in basket1:
            if c1[x] == c2[x]:
                best_min = min(best_min, x)

        ans = 0
        while s1 and s2:
            
            p1 = s1.pop()
            p2 = s2.pop()
            q1, q2 = c1[p1], c2[p2]

            # compute the swap count for each stack
            swc1 = (q1 - c2[p1]) // 2
            swc2 = (q2 - c1[p2]) // 2
            swap = min(swc1, swc2)

            # compute the cost of swap
            # 1) direct swap
            op1 = swap * min(p1, p2)
            # 2) indirect swap
            op2 = 2 * swap * best_min

            ans += min(op1, op2)

            # perform swaps
            c1[p1] -= swap
            c2[p1] += swap

            c2[p2] -= swap
            c1[p2] += swap

            # append imbalanced items back
            if c1[p1] > c2[p1]:
                s1.append(p1)
            elif c1[p1] == c2[p1]:
                # potential improved best_min
                best_min = min(best_min, p1)

            if c2[p2] > c1[p2]:
                s2.append(p2)
            elif c2[p2] == c1[p2]:
                best_min = min(best_min, p2)

        if s1 or s2: return -1
        return ans
    
basket1, basket2 = [4,2,2,2], [1,4,1,2]
basket1, basket2 = [2,3,4,1], [3,2,5,1]
basket1, basket2 = [84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]

Solution().minCost(basket1, basket2)