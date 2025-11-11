# dp - medium
from typing import List
from functools import cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    
        N = len(strs)
        # pre-compute the number of zeros / ones in each string
        cnt = []
        for i in range(N):
            z = strs[i].count('0')
            o = len(strs[i]) - z
            cnt.append([z, o])
        
        @cache
        def f(i, zeros, ones):

            if i == N:
                return 0
            
            c0, c1 = cnt[i][0], cnt[i][1]
            
            res = 0
            # take option
            if c0 + zeros <= m and c1 + ones <= n:
                res = max(res, 1 + f(i+1, c0 + zeros, c1 + ones))

            # skip option
            res = max(res, f(i+1, zeros, ones))

            return res

        return f(0, 0, 0)

strs, m, n = ["10","0001","111001","1","0"], 5, 3
strs, m, n = ["10","0","1"], 1, 1
strs, m, n = ["101000000","1100001010","11101000","011010110","0010001","0011","0111101111"], 10, 11
strs, m, n = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0"
              ,"11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80

Solution().findMaxForm(strs, m, n)