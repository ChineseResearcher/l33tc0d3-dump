# graph - medium
### O(n*inverseAckerman(n)) ≈ O(n) solution - slow ###
import copy
from collections import defaultdict, Counter
from typing import List
class UnionFind:
    def __init__(self, n):
        # Initialize the Union-Find structure with n elements
        self.parent = list(range(n))  
        self.rank = [1] * n           

    def find(self, x):
        # Find with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        # first collect each unique number's occurrence indices into a dict
        joinRight = defaultdict(list)
        for i, x in enumerate(nums):
            joinRight[x].append(i)

        joinLeft = copy.deepcopy(joinRight)
        num_set = list(joinRight.keys())

        # create a dsu of size n
        dsu = UnionFind(n)

        # explore each number and union with next consecutive number (if any)
        for x in num_set:

            while joinRight[x]:

                if not joinLeft[x+1]:
                    break
                i, j = joinRight[x].pop(), joinLeft[x+1].pop()
                dsu.union(i, j)
                if not joinLeft[x+1]:
                    del joinLeft[x+1]

            while joinLeft[x]:

                if not joinRight[x-1]:
                    break
                i, j = joinLeft[x].pop(), joinRight[x-1].pop()
                dsu.union(i, j)
                if not joinRight[x-1]:
                    del joinRight[x-1]

        # make sure all paths have been compressed
        for i in range(n):
            dsu.find(i)

        return max(Counter(dsu.parent).values())

### O(n) solution - fast ###
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        ans = 0

        # explore every unique number as the potential start
        for n in num_set:

            # a valid start should have no smaller consecutive
            if n-1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1

                if length > ans:
                    ans = length

        return ans
    
nums = [1,0,1,2]
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

Solution().longestConsecutive(nums)