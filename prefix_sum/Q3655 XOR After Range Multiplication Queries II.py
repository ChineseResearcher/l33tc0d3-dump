# prefix sum - hard
import math
from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) We cannot simply simulate by iterating [L,R] on each query
        # 2) use sqrt decomposition for queries with step size k <= sqrt(n), and
        # build diff array(s) to record the range updates based on paired keys (k, L mod k)
        B = 100
        upd = dict()

        MOD = int(1e9 + 7)
        for L, R, k, v in queries:
            
            if k <= B:
                gkey = (k, L % k)
                if gkey not in upd:
                    upd[gkey] = [1] * math.ceil(n/k)

                d = upd[gkey]
                
                i = L // k
                d[i] *= v
                d[i] %= MOD

                j = i + (R - L) // k + 1
                if j < len(d):
                    d[j] *= pow(v, -1, MOD)

            else:
                for i in range(L, R + 1, k):
                    nums[i] *= v
                    nums[i] %= MOD

        # obtain prefix cumulative product on assigned updates
        for diff_arr in upd.values():
            diff_arr[0] %= MOD
            for i in range(1, len(diff_arr)):
                diff_arr[i] = diff_arr[i] * diff_arr[i-1]
                diff_arr[i] %= MOD    

        # perform a sweep across all k <= B for every index [0...n-1]
        # and collect the updates by accessing upd[(k, i % k)]
        for i in range(n):
            for k in range(1, B + 1):
                gkey = (k, i % k)
                if gkey in upd:
                    nums[i] *= upd[gkey][i//k]
                    nums[i] %= MOD

        XOR = 0
        for x in nums:
            XOR ^= x

        return XOR

nums, queries = [1,1,1], [[0,2,1,4]]
nums, queries = [2,3,1,5,4], [[1,4,2,3],[0,2,1,2]]

Solution().xorAfterQueries(nums, queries)