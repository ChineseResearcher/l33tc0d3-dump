# string - medium
from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        # helper to build prefixes based on a list of integers
        def get_pf(arr: List[int]) -> set:
            res = set()
            for x in arr:
                x_str = str(x)
                for i in range(1, len(x_str)+1):
                    res.add(int(x_str[:i]))
            return res

        arr1_pf, arr2_pf = get_pf(arr1), get_pf(arr2)

        # common prefixes
        c = arr1_pf & arr2_pf

        ans = 0
        for x in c:
            ans = max(ans, len(str(x)))

        return ans

arr1, arr2 = [1,10,100], [1000]
arr1, arr2 = [1,2,3], [4,4,4]

Solution().longestCommonPrefix(arr1, arr2)