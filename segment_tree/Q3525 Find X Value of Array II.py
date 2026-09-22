# segment tree - hard
class Node:
    __slots__ = ("prod", "pref")

    def __init__(self, k, val=None):
        self.prod = 0
        self.pref = [0] * k

        if val is not None:
            p = val % k
            self.prod = p
            self.pref[p] = 1

class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.nums = nums

        self.tree = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _merge(self, A, B):
        k = self.k
        C = Node(k)

        # Product of entire A + B
        C.prod = A.prod * B.prod % k

        # Prefixes entirely inside A
        for p in range(k):
            C.pref[p] = A.pref[p]

        # Prefixes that consume all of A and then
        # take a prefix of B
        for b in range(k):
            if B.pref[b]:
                p = A.prod * b % k
                C.pref[p] += B.pref[b]

        return C

    def _build(self, node, l, r):
        if l == r:
            self.tree[node] = Node(self.k, self.nums[l])
            return

        mid = (l + r) // 2

        self._build(node * 2, l, mid)
        self._build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self._merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, idx, value):
        self.nums[idx] = value
        self._update(1, 0, self.n - 1, idx, value)

    def _update(self, node, l, r, idx, value):
        if l == r:
            self.tree[node] = Node(self.k, value)
            return

        mid = (l + r) // 2

        if idx <= mid:
            self._update(node * 2, l, mid, idx, value)
        else:
            self._update(node * 2 + 1, mid + 1, r, idx, value)

        self.tree[node] = self._merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        if qr <= mid:
            return self._query(
                node * 2, l, mid, ql, qr
            )

        if ql > mid:
            return self._query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

        left = self._query(
            node * 2, l, mid, ql, qr
        )

        right = self._query(
            node * 2 + 1, mid + 1, r, ql, qr
        )

        return self._merge(left, right)

    def count(self, l, r, x):
        """
        Number of subarrays

            [l, l], [l, l+1], ..., [l, r]

        whose product % k == x.
        """
        return self.query(l, r).pref[x]

from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        
        n = len(nums)
        ST = SegmentTree(nums, k)
        
        ans = []
        for i, v, si, x in queries:
            ST.update(i, v)
            ans.append(ST.count(si, n - 1, x))

        return ans

nums, k, queries = [1,1,2,1,1], 2, [[2,1,0,1]]
nums, k, queries = [1,2,4,8,16,32], 4, [[0,2,0,2],[0,2,0,1]]
nums, k, queries = [1,2,3,4,5], 3, [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Solution().resultArray(nums, k, queries)