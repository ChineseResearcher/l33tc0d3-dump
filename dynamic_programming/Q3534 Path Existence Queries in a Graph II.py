# dp - hard
from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        # key ideas:
        # 1) Sliding Window + Greedy to determine next array
        # 2) Binary Lifting pre-computation to speed up query
        m1, m2 = dict(), dict()
        # 1) map index to val for original nums
        # 2) map val to index for de-dup nums 
        for i in range(n):
            m1[i] = nums[i]

        dnums = sorted(set(nums))
        for i in range(len(dnums)):
            m2[dnums[i]] = i

        def findNext(arr: List[int], k:int) -> List[int]:
            '''
            Given an array containing ascending distinct numbers,
            find the leftmost arr[l] for each arr[r] s.t. 
            arr[r] - arr[l] <= k
            '''
            m = len(arr)

            # default to dummy -1
            nxt = [-1] * m

            l = 0
            for r in range(m):
                while arr[r] - arr[l] > k:
                    l += 1
                # when there is no next best, next[arr[i]] is set to itself
                nxt[r] = l

            return nxt

        nxt = findNext(dnums, maxDiff)

        # build binary lifting table using DP recurrence
        m = len(nxt)
        LOG = (m - 1).bit_length()

        up = [ [-1] * LOG for _ in range(m) ]
        for i in range(m):
            if nxt[i] != -1 and nxt[i] < i:
                up[i][0] = nxt[i]

        for j in range(1, LOG):
            for i in range(m):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]

        ans = []
        # process each query in O(logN) time
        for i, j in queries:

            if i == j:
                ans.append(0)
                continue

            a, b = m1[i], m1[j]
            if a == b:
                ans.append(1)
                continue

            a_i, b_i = m2[a], m2[b]
            # enforce idx(a) > idx(b)
            if b_i > a_i: a_i, b_i = b_i, a_i

            curr, res = a_i, 0
            # take the largest jump(s) that still do NOT reach b
            for j in reversed(range(LOG)):
                upNext = up[curr][j]
                if upNext > b_i:
                    curr = upNext
                    res += (1 << j)

            # one final move to cross below "b"
            if -1 < up[curr][0] <= b_i:
                ans.append(res + 1)
            else:
                ans.append(-1)

        return ans

n, nums, maxDiff, queries = 5, [1,8,3,4,2], 3, [[0,3],[2,4]]
n, nums, maxDiff, queries = 3, [3,6,1], 1, [[0,0],[0,1],[1,2]]
n, nums, maxDiff, queries = 5, [5,3,1,9,10], 2, [[0,1],[0,2],[2,3],[4,3]]

Solution().pathExistenceQueries(n, nums, maxDiff, queries)