# number theory - medium
import math
from collections import Counter
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) perform a freq. count first, if there's at least one of "1"
        # then we could "broadcast" this to neighbour values
        # e.g. [1,a,a,1,a,1] would take three operations to achieve all "1"s

        # 2) if there's no occurrence of "1", we check gcd of each consecutive pair
        # and as long as we have one pair that yields gcd = 1, we could turn the
        # arr. into all "1"s in deterministic number of steps

        f = Counter(nums)
        if f[1] > 0:
            return n - f[1]

        # as a special case of (2), we would always be able to
        # reduce the whole arr. to "1"s in n steps if any consecutive pair of 
        # the original arr. has gcd = 1 directly
        for i in range(n-1):
            if math.gcd(nums[i], nums[i+1]) == 1:
                return n

        def help(startIdx: int, forward: bool) -> int:

            arr = nums[:] if forward else nums[::-1]
            if not forward:
                startIdx = n - startIdx - 1
            # track reduction operations
            ops = 0

            for i in range(startIdx, n-1):
                k = math.gcd(arr[i], arr[i+1])
                if k == 1:
                    # total cost = i + (n-i) + ops = n + ops
                    return n + ops
                
                # otherwise, partial reduction happens for arr[i+1]
                ops += 1 if arr[i+1] != k else 0
                arr[i+1] = k

            return float('inf')
        
        ans = float('inf')
        # test every index i as the potential starting index
        # and test with forward / backward scans
        for i in range(n):
            f_res, b_res = help(i, True), help(i, False)
            ans = min(ans, min(f_res, b_res))

        return ans if ans < float('inf') else -1
    
nums = [2,6,3,4]
nums = [2,10,6,14]
nums = [6,10,15]
nums = [10,15,5,60,21]
nums = [15,10,15,6,3]

Solution().minOperations(nums)