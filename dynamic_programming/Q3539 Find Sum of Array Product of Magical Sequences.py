# dp - hard
from typing import List
from functools import cache
class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        # pre-compute nCk
        C = [ [0] * (M+1) for _ in range(M+1) ]
        for i in range(M + 1):
            for j in range(i + 1):
                if j == 0:
                    C[i][j] = 1
                else:
                    C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        @cache
        def f(mask, m, k, depth): # return: sum of prods

            # have formed seq of length-m
            if m == 0:
                return 1 if mask.bit_count() == k else 0

            # have exhausted all available numbers from range [0,1,2,...,n-1]  
            if depth == len(nums):
                return 0
            
            res = 0
            # op1: skip curr. number (depth)
            res += f(mask >> 1, m, k - (mask & 1), depth + 1)
            # op2: pick 'c' copies of curr. number
            for c in range(1, m+1):
                nmask = mask + c
                nm = m - c
                nk = k - (nmask & 1)
                sp = f(nmask >> 1, nm, nk, depth + 1)
                
                # get multiplication res
                curr_res = sp * pow(nums[depth], c, MOD)
                # combinatorics application:
                # Choose "c" copies out of "m" copies -> m!/(c!*(m-c)!)
                curr_res *= C[m][c]

                res += curr_res 
                res %= MOD

            return res
        
        return f(0, M, K, 0) % MOD

m, k, nums = 5, 5, [1,10,100,10000,1000000]
m, k, nums = 2, 2, [5,4,3,2,1]
m, k, nums = 1, 1, [28]
# constraint
m, k, nums = 30, 30, [i for i in range(1, 51)]

Solution().magicalSum(m, k, nums)