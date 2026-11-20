# number theory - hard
from collections import defaultdict
maxN = int(1e4)
g = defaultdict(list)
start, rem = 1, [i for i in range(2, maxN + 1)]
while rem:
    ng, nrem = [start], []
    for i in rem:
        p = i * ng[-1]
        r = int(p ** 0.5)
        if pow(r, 2) == p:
            ng.append(i)
        else:
            nrem.append(i)
    # note that for some primes, it will not be able
    # to form any complete subset with size > 1
    if len(ng) > 1:
        g[ng[0]] = ng
    rem = nrem[1:]
    start = nrem[0]

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        
        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) observe that the concept of finding a subgroup of indices s.t. each
        # pair is a perfect square when multiplied is similar to union-find. As such,
        # there will be no overlap of complete subset(s)
        # 2) pre-compute the complete subsets by considering N <= 1e4, and 
        # exploit the property stated in (1) to find the max sum of a complete subset

        ans = 0
        for k in g.keys():
            s = 0
            for x in g[k]:
                if x > n:
                    break
                s += nums[x - 1]
            ans = fmax(ans, s)

        return ans

nums = [8,7,3,5,7,2,4,9]
nums = [8,10,3,8,1,13,7,9,4]

Solution().maximumSum(nums)