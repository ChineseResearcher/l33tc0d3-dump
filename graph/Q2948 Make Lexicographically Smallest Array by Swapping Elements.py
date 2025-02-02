# graph - medium
from collections import deque
class Solution:
    # this question should be rated hard according to contest rating
    # the challenge is to do it in O(N^LogN) time by relying on sorting
    # and leveraging on the concept of a Disjoint Set Union (DSU)
    def lexicographicallySmallestArray(self, nums, limit):
        
        n = len(nums)
        # construct a parent arr. (a key idea in DSU) for indicate
        # the parent cluster nums[i] belongs to (initially every num is on its own)
        parent = [i for i in range(n)]

        # initiate a cluster dict
        cluster = dict()

        nums_sorted = sorted([[num, idx] for idx, num in enumerate(nums)])
        # first cluster is assigned to the first element in nums_sorted
        cluster[parent[nums_sorted[0][1]]] = deque([nums_sorted[0][0]])

        for i in range(1, n):

            currNum, currIdx = nums_sorted[i][0], nums_sorted[i][1]
            # check limit cond.
            if abs(currNum - nums_sorted[i-1][0]) <= limit:
                # assign new parent
                parent[currIdx] = parent[nums_sorted[i-1][1]]
                cluster[parent[currIdx]].append(currNum)

            else:
                # do not assign new parent
                # but create a new cluster head
                cluster[parent[currIdx]] = deque([currNum])

        for i in range(n):

            # check final parent of the current idx
            finalParent = parent[i]

            # assign the smallest val. in this cluster, which is leftmost of deque
            nums[i] = cluster[finalParent].popleft()

        return nums
    
nums, limit = [1,5,3,9,8], 2
nums, limit = [1,7,6,18,2,1], 3
nums, limit = [1,7,28,19,10], 3

Solution().lexicographicallySmallestArray(nums, limit)