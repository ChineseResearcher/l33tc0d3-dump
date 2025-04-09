# counting - medium
from collections import defaultdict
class Solution:
    def destroyTargets(self, nums, space):
        # for nums[i], all nums[j] s.t. nums[j] = nums[i] + c * space
        # can be destroyed, and we can efficiently identify groups of
        # numbers using the modulo result w/ space

        # dict stores <mod_res, [cnt, min_num in this grp]>
        mod_grp = defaultdict(list)

        for num in nums:
            
            if not mod_grp[num % space]:
                mod_grp[num % space].extend([1, num])
            else:
                mod_grp[num % space][0] += 1
                mod_grp[num % space][1] = min(mod_grp[num % space][1], num)

        max_grp, min_seed = 0, float('inf')
        for _, v in mod_grp.items():

            if v[0] > max_grp:
                max_grp = max(max_grp, v[0])
                min_seed = v[1]
            elif v[0] == max_grp:
                min_seed = min(min_seed, v[1])

        return min_seed
    
nums, space = [3,7,8,1,1,5], 2
nums, space = [1,3,5,2,4,6], 2
nums, space = [6,2,5], 100
nums, space = [1,5,3,2,2], 10000

Solution().destroyTargets(nums, space)