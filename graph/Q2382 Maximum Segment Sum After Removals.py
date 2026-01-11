# graph - hard
from collections import defaultdict
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
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        n = len(nums)
        # key ideas:
        # 1) construct a DSU as we reverse-process the removeQueries
        # or in other words, we are building up segments towards full nums

        # 2) segments that touch each other become contiguous and thus union-ed
        # and we track an array "active" to indicate if nums[i] is already built
        uf = UnionFind(n)
        active = [False] * n

        # to obtain the answer we track the total sum accumulated in each union
        union_sum = defaultdict(int)

        fmax = lambda a, b: a if a > b else b

        currMax, ans = 0, [0]
        for i in range(n-1, 0, -1):

            j = removeQueries[i]
            active[j] = True

            # determine if left and right are activated
            l_active = True if (j-1 >= 0 and active[j-1]) else False
            r_active = True if (j+1 < n and active[j+1]) else False

            # 4 scenarios for possible update of union_sum
            if l_active and r_active:
                uf.find(j-1)
                uf.find(j)
                uf.find(j+1)
                # compute aggregated sum
                new_sum = union_sum[uf.parent[j-1]] + nums[j] + union_sum[uf.parent[j+1]]
                # union left + curr + right
                uf.union(j-1, j)
                uf.union(j-1, j+1)
                uf.find(j-1)
                uf.find(j)
                uf.find(j+1)
                # assign new aggregated sum to new parent
                union_sum[uf.parent[j]] = new_sum
                currMax = fmax(currMax, new_sum)
                
            elif l_active:
                uf.find(j-1)
                uf.find(j)
                new_sum = union_sum[uf.parent[j-1]] + nums[j]
                uf.union(j-1, j)
                uf.find(j-1)
                uf.find(j)
                union_sum[uf.parent[j]] = new_sum
                currMax = fmax(currMax, new_sum)

            elif r_active:
                uf.find(j+1)
                uf.find(j)
                new_sum = union_sum[uf.parent[j+1]] + nums[j]
                uf.union(j+1, j)
                uf.find(j+1)
                uf.find(j)
                union_sum[uf.parent[j]] = new_sum
                currMax = fmax(currMax, new_sum)
                
            else:
                new_sum = nums[j]
                union_sum[uf.parent[j]] = new_sum
                currMax = fmax(currMax, new_sum)

            ans.append(currMax)

        return ans[::-1]

nums, removeQueries = [1,2,5,6,1], [0,3,2,4,1]
nums, removeQueries = [3,2,11,1], [3,2,1,0]

Solution().maximumSegmentSum(nums, removeQueries)