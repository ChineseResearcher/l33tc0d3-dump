# sorting - medium
from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        # key ideas:
        # 1) build an auxiliary array based on the mapping
        # 2) sort original nums array using the auxiliary array built
        m = dict()
        for i in range(10):
            m[str(i)] = str(mapping[i])

        aux = []
        for x in nums:
            t = []
            for y in str(x):
                t.append(m[y])
            aux.append(int(''.join(t).lstrip()))
        
        return [nums[x] for _, x in sorted(zip(aux, [i for i in range(len(nums))]))]

mapping, nums = [8,9,4,0,2,1,3,5,7,6], [991,338,38]
mapping, nums = [0,1,2,3,4,5,6,7,8,9], [789,456,123]

Solution().sortJumbled(mapping, nums)