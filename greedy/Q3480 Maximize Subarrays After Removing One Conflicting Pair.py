# greedy - hard
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        # groups[i] stores all conflicts (i, j) w/ j > i
        groups = defaultdict(list)
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)

        # extra[j] represents the number of subarrays to gain
        # if a conflict pair (i, j) with j > i is deleted
        # note: we need length 1 + n + 1 = n + 2 (j = 0 and j = n + 1 as dummy)
        extra = [0] * (n + 2)

        # right is initiated to size 2, with right[0] = right[1] = n + 1
        # to indicate that there's no nearest conflict on the RHS at the start
        right = [n + 1, n + 1]  

        ans = 0
        # enumerate our left pointer i in reverse order
        for i in range(n, 0, -1):

            # for every i, we've already stored all j s.t. j > i and (i, j) is a conflict pair
            # we then collect all such conflict pairs in "right"
            right.extend(groups[i]) 
            # two relevant right violations to account for (greedy thinking):
            # (1) the nearest violation and (2) the second nearest violation
            right.sort() 
            right = right[:2]

            # assuming no deletion possible, we could have valid subarr.
            # [i], [i, i+1], [i, i+1, i+2], ..., [i, i+1, i+2, .., right[0]-1]
            ans += right[0] - i

            # document the extra to gain if some conflict 
            # pairs (i, j) with j = right[0] is deleted
            # note: index by "right[0]" not "i" because there can be multiple "i"s
            # at which the nearest RHS violation is the same "right[0]"
            extra[right[0]] += right[1] - right[0]

        return ans + max(extra)
    
n, conflictingPairs = 4, [[1,3],[2,3],[1,4]]
n, conflictingPairs = 5, [[1,2],[2,5],[3,5]]

Solution().maxSubarrays(n, conflictingPairs)