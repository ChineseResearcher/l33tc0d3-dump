# segment tree - hard
import heapq
from typing import List
fmin = lambda a, b: a if a < b else b
fmax = lambda a, b: a if a > b else b
class SegmentTree:
    def __init__(self, arr):

        self.n = len(arr)
        self.size = 1 << self.n.bit_length()

        INF = float('inf')
        self.tree_min = [INF] * (2 * self.size)
        self.tree_max = [-INF] * (2 * self.size)

        # build leaves
        for i in range(self.n):
            self.tree_min[self.size + i] = arr[i]
            self.tree_max[self.size + i] = arr[i]

        # build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree_min[i] = fmin(
                self.tree_min[2 * i],
                self.tree_min[2 * i + 1]
            )
            self.tree_max[i] = fmax(
                self.tree_max[2 * i],
                self.tree_max[2 * i + 1]
            )

    def query(self, l, r, mode):
        l += self.size
        r += self.size

        res = float('inf') if mode == 'min' else float('-inf')
        f = fmin if mode == 'min' else fmax
        v = self.tree_min if mode == 'min' else self.tree_max

        while l <= r:
            if l % 2 == 1:
                res = f(res, v[l])
                l += 1

            if r % 2 == 0:
                res = f(res, v[r])
                r -= 1

            l //= 2
            r //= 2

        return res

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # key ideas:
        # 1) for each fixed "l", the result of max(l, r) - min(l, r) is non-decreasing
        # as we increment r from r = l+1 to r = n-1
        # 2) we could then initiate a maxHeap storing all (l, n-1) for l in range [0, n-2]
        # as the starting candidates, which must contain max. diff. (l, r) pairs
        # 3) each time we obtain the curr. best candidate (l0, r0), we propose a new
        # candidate (l0, r0-1) by inserting into the maxHeap
        # 4) the querying of max(l, r) - min(l, r) is made efficient by segment tree

        ST = SegmentTree(nums)

        maxHeap = []
        for l in range(n-1):
            res = ST.query(l, n-1, 'max') - ST.query(l, n-1, 'min') 
            heapq.heappush(maxHeap, (-res, l, n-1))

        ans = 0
        while k > 0 and maxHeap:

            diff, l, r = heapq.heappop(maxHeap)
            ans += abs(diff)
            # next candidate
            if r - 1 > l: 
                res = ST.query(l, r-1, 'max') - ST.query(l, r-1, 'min') 
                heapq.heappush(maxHeap, (-res, l, r-1))
            k -= 1
            
        return ans
    
nums, k = [1,3,2], 2
nums, k = [4,2,5,1], 3

Solution().maxTotalValue(nums, k)