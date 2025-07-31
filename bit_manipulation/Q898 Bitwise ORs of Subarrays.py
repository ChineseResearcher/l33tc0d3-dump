# bit manipulation - medium
from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        n = len(arr)
        # core idea:
        # 1) bitwise OR is monotonic, we can build a prefix bitwise OR set (not arr!)

        # 2) processing the prefix OR set is O(32) -> constant time because there are 
        # at most 32 unique 0Rs in the set at any time
        # i.e. prefix OR only contains the unique ORs from [0...i-1], [1...i-1], ..., [i-1]
        # at any time, and the probability space for unique ORs is at most 32 
        # because it is impossible for unique ORs like 0b1101 and 0b0010 to co-exist

        # 3) init. another set storing all encountered bitwise ORs
        ans = set()

        prefix_OR = set([0])
        for x in arr:

            curr_OR = set()
            while prefix_OR:
                curr_OR.add(x | prefix_OR.pop())
            curr_OR.add(x)

            # add to answers
            ans |= curr_OR

            # merge two sets
            prefix_OR |= curr_OR

        return len(ans)
    
arr = [0]
arr = [1,1,2]
arr = [1,2,4]

Solution().subarrayBitwiseORs(arr)