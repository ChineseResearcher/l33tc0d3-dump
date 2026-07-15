# number theory - hard
from typing import List
from collections import Counter
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        # key ideas:
        # 1) apply Number Theory to find count of pairs with gcd = i for i in range [1, max(nums)]
        # 2) use Prefix Sum + Binary Search to obtain the gcd result for each query
        V = max(nums)

        freq = Counter(nums)
        # cnt[i] records the count of array elements divisible by i
        cnt = [0] * (V + 1)
        for d in range(1, V + 1):
            for multiple in range(d, V + 1, d):
                cnt[d] += freq[multiple]

        exact = [0] * (V + 1)
        # suppose we denote F(i) as the count of pairs whose gcd is i, OR a multiple of i
        # then we can use inclusion-exclusion principle to obtain exactly
        # the count of pairs where gcd = i
        # e.g. exact[i] = F(i) - F(2 * i) - F(3 * i) - ... - F(k * i) subject to k * i <= V
        # note: we need to iterate divisors backwards to ensure proper filling of values
        for i in range(V, 0, -1):

            # cnt of All pairs divisible by d
            c = cnt[i]
            F_i = c * (c - 1) // 2 # choose pairs out of c members

            res = F_i
            # remove pairs whose gcd is a larger multiple of d
            multiple = 2 * i
            while multiple <= V:
                res -= exact[multiple]
                multiple += i

            exact[i] = res

        # build a prefix sum on the gcd-exact-cnt array
        pf_cnt = [exact[0]]
        for i in range(1, V + 1):
            pf_cnt.append(pf_cnt[-1] + exact[i])

        ans = []
        for q in queries:
            q += 1 # 1-indexed
            
            l, r = 1, V # binary search on [1, V]
            while l <= r:
                mid = (l + r) >> 1
                if q > pf_cnt[mid]:
                    l = mid + 1
                elif q <= pf_cnt[mid - 1]:
                    r = mid - 1
                else:
                    ans.append(mid)
                    break
            
        return ans
    
nums, queries = [2,2], [0,0]
nums, queries = [2,3,4], [0,2,2]
nums, queries = [4,4,2,1], [5,3,1,0]

Solution().gcdValues(nums, queries)