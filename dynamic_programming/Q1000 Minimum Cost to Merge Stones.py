# dp - hard
from typing import List
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        # if there's only one stone, it's already in the one pile state we want
        if n == 1:
            return 0

        # if we want to merge n stones by considering k consecutive stones, where
        # n = k, there's only one way to merge it
        if n == k:
            return sum(stones)

        # build pfsum for stones
        pfSum, rSum = [], 0
        for s in stones:

            rSum += s
            pfSum.append(rSum)

        dp = dict()
        def recursive_merge(l, r, p):

            # p refers to the number of piles to want for the curr. stones[l..r]
            if l == r:
                
                ## fail check (1)
                # note that we do not incur merge cost if we want 1 pile from only 1 stone
                return 0 if p == 1 else float('inf')

            ## fail check (2)
            # also it's impossible to form "p" piles if we have less than "p" stones
            # i.e. the max. piles we can form from "n" stones is "n" piles
            if r-l+1 < p:
                return float('inf')            

            if (l, r, p) in dp:
                return dp[(l, r, p)]
            
            if p == 1:
                
                ## fail check (3)
                # observe that every time we merge k consecutive stone piles
                # the length reduces by k-1, we can tell if the current range length would 
                # result in a final length-1 pile with the following
                if (r-l) % (k-1) == 0:  

                    # compute the one-pile-cost (opc)
                    opc = pfSum[r] - pfSum[l-1] if l > 0 else pfSum[r]

                    # the beauty of this transition is that if we are looking at merging
                    # some stones into 1 pile, it is equivalent to finding what's the cost
                    # to convert it to k piles first so that we can merge as 1 pile

                    # we have to formulate it this way as we are constrained by the problem
                    # s.t. every merge we do has to respect "k" consecutive stones
                    return recursive_merge(l, r, k) + opc

                return float('inf')

            curr_res = float('inf')
            # explore split j s.t. we are dividing the current range into subproblems: 
            # left problem: 1 pile; right problem: (p-1) piles
            for j in range(l, r):

                left = recursive_merge(l, j, 1)
                right = recursive_merge(j+1, r, p-1)
                curr_res = min(curr_res, left + right)
                
            dp[(l, r, p)] = curr_res
            return curr_res

        # what's the cost of merge all stones into 1 pile?
        final_res = recursive_merge(0, n-1, 1)
        return final_res if final_res < float('inf') else -1
    
stones, k = [3,2,4,1], 2
stones, k = [3,2,4,1], 3
stones, k = [3,5,1,2,6], 3
stones, k = [1,2,3,4,5], 3
stones, k = [4,6,4,7,5], 2
stones, k = [8,8,9,1,7,2,4,3], 2

Solution().mergeStones(stones, k)