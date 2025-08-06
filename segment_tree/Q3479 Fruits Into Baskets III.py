# segment tree - medium
from typing import List
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # why 4 * self.n ?
        # 1) segment tree is a binary tree
        # 2) full binary tree with n leaves can have up to 2n - 1 nodes
        # 3) 4n is just a safe upper bound
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(index, value, 2 * node + 1, start, mid)
            else:
                self.update(index, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    # binary search for minimum index of large enough x to place fruit
    def bs(self, target, node=0, start=0, end=None):
        if end is None:
            end = self.n-1

        # we don't have to drill into the leaf node to get an answer
        # this earlyStop optimisation is crucial
        if self.tree[node] < target:
            return float('inf')

        if start == end:
            return start if self.tree[node] >= target else float('inf')
        
        mid = (start + end) // 2
        left_max = self.bs(target, 2 * node + 1, start, mid)
        if left_max < self.n:
            return left_max

        right_max = self.bs(target, 2 * node + 2, mid + 1, end)
        if right_max < self.n:
            return right_max

        return float('inf')

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        # core ideas:
        # 1) build a segment tree based on baskets, w/ each node storing the max of the range
        # 2) for each fruit, find the index of the leftmost basket that can place the fruit
        st = SegmentTree(baskets)

        k = len(fruits)
        for x in fruits:
            min_idx = st.bs(x)
            if min_idx < float('inf'):
                # successful placement
                st.update(min_idx, 0)

                k -= 1

        return k
    
fruits, baskets = [4,2,5], [3,5,4]
fruits, baskets = [3,6,1], [6,4,7]
# test max input length
import random
random.seed(2025)
fruits = [random.randint(1, int(1e9)) for _ in range(int(1e5))]
baskets = [random.randint(1, int(1e9)) for _ in range(int(1e5))]

Solution().numOfUnplacedFruits(fruits, baskets)