# greedy - medium
from typing import List
from collections import Counter
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        # idea is to count the number of zeroes in each array first
        # and calculate the minimum base num for both arrays
        n1c, n2c = Counter(nums1), Counter(nums2)

        # the minimum base num for nums1 is the sum of nums1, 
        # adding the count of 0s in nums1, as this is the minimum sum
        # of nums1 arr. if all 0s are to turn strictly positive (per question requires)
        s1, s2 = sum(nums1), sum(nums2)
        mb1, mb2 = s1 + n1c[0], s2 + n2c[0]

        # take care of cases where no 0s in either arrays or both
        if n1c[0] == 0 and n2c[0] == 0:
            return s1 if s1 == s2 else -1

        if n1c[0] == 0:
            # no way for s1 to match up to mb2 if no 0s in nums1
            return s1 if mb2 <= s1 else -1

        if n2c[0] == 0:
            return s2 if mb1 <= s2 else -1

        # LOGIC for getting answer:
        # if mb1 is chosen as the basis for equal sum, then the surplus
        # from mb1 - sum(nums2) must be spread across all 0s in nums2, vice versa
        # Note: up to here there are definitely 0s in BOTH arrays
        ans = float('inf')
        if mb1 - s2 >= n2c[0]:
            ans = min(ans, mb1)
        if mb2 - s1 >= n1c[0]:
            ans = min(ans, mb2)

        return ans if ans < float('inf') else -1
    
nums1, nums2 = [3,2,0,1,0], [6,5,0]
nums1, nums2 = [2,0,2,0], [1,4]

Solution().minSum(nums1, nums2)