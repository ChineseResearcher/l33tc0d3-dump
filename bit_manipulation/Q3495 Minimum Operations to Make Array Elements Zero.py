# bit manipulation - medium
from typing import List
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        # helper to obtain the total no. of reductions needed for range [l, r]
        # e.g. for range [2,4], we have [2,3,4], and correspondingly we would
        # need [1,1,2] reductions respectively, and thus reduction total = 4
        def get_reduc_cnt(l, r):

            reduc_cnt = 0
            # identify the nearest upper bound for the power of 4
            # e.g., 5 is lower bounded by 4^2; 17 is lower bounded by 4^3
            msb = l.bit_length() - 1

            # nearest upper bound (nub)
            nub = (msb if msb % 2 == 0 else msb + 1) // 2
            if pow(4, nub) <= l:
                nub += 1

            # print(f'starting bounding power of 4:', nub)

            if r < pow(4, nub):
                return (r - l + 1) * nub
            
            # take care of left bound counting
            reduc_cnt += (pow(4, nub) - l) * nub

            nub += 1
            while r >= pow(4, nub):
                reduc_cnt += (pow(4, nub) - pow(4, nub-1)) * nub
                nub += 1

            # make sure 4^nub <= r
            if pow(4, nub) > r:
                nub -= 1

            # take care of right bound counting
            reduc_cnt += (r - pow(4, nub) + 1) * (nub + 1)

            return reduc_cnt
        
        ans = 0
        for l, r in queries:

            no_of_reduc = get_reduc_cnt(l, r)
            if no_of_reduc % 2 == 0:
                curr_ans = no_of_reduc // 2
            else:
                curr_ans = (no_of_reduc // 2) + 1

            ans += curr_ans
        
        return ans
    
queries = [[1,2],[2,4],[1,4],[2,6]]
queries = [[1,int(1e9)] for _ in range(int(1e5))] # constraint

Solution().minOperations(queries)