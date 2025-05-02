# greedy - medium
from typing import List
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        # we rely on the property that bitwise & only remains the same
        # OR reduces as we include more numbers, so as long as our cumulative
        # bitwise & remains above 0, we keep expanding our curr. group
        curr_AND, grp_cnt = None, 0

        for i in range(n):

            if curr_AND is None:
                curr_AND = nums[i]

                # all '0' should be greedily made a group itself
                # this is because local optimality -> global optimality
                if curr_AND == 0:
                    grp_cnt += 1
                    curr_AND = None

                continue

            curr_AND &= nums[i]

            if curr_AND == 0:
                grp_cnt += 1
                # reset curr_AND
                curr_AND = None

        # if our last group is non-zero, means we would need to 
        # undo the creation of the last group, and merge w/ the prev. group to become 0
        if curr_AND is not None and curr_AND > 0:

            # only merge if there's a prev. group to merge w/
            if grp_cnt > 0:
                grp_cnt -= 1

            # otherwise, there's only one grp
            grp_cnt += 1

        return grp_cnt
    
nums = [1,0,2,0,1,2]
nums = [5,7,1,3]
nums = [1,0,0,0]
nums = [0,8,0,0,0,23]
nums = [8,10,23,26,21,28,21,14,21,14,9,16,24,29,7,26]
nums = [0,0,18,0,0,4,5,25,0,0,0,30,0,18,0,0,12,21,21,18]

Solution().maxSubarrays(nums)