# heap - medium
import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m, n = len(nums1), len(nums2)
        # key ideas:
        # 1) we start with (nums1[0], nums2[0]) as the global min. pair
        # 2) greedily propose the next TWO best pairs (nums1[i+1], nums2[j])
        # and (nums1[i], nums2[j+1]) by insertion into a minHeap
        # 3) avoid solving the same subproblems by hashsing (i, j)
        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        solved = set([(0, 0)])

        ans = []
        while k > 0:

            _, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            # explore next 2 pairs
            if i + 1 < m and (i+1, j) not in solved:
                solved.add((i+1, j))
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j))

            if j + 1 < n and (i, j+1) not in solved:
                solved.add((i, j+1))
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1))

            k -= 1

        return ans

nums1, nums2, k = [1,1,2], [1,2,3], 2
nums1, nums2, k = [1,7,11], [2,4,6], 3
nums1, nums2, k = [1,2,4,5,6], [3,5,7,9], 20

Solution().kSmallestPairs(nums1, nums2, k)