# greedy - hard
from typing import List
from collections import defaultdict
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)
        # key ideas:
        # 1) for all chunks after sorting and concatenation, they need to
        # produce the same sorted array that is obtained by sorting arr. directly
        # 2) we cannot split another chunk at i, if the max. sorted index of any
        # elements in curr. chunk exceeds i

        # perform sorting and record the indices of each distinct number
        sarr, p = sorted(arr), defaultdict(list)
        for i in range(n - 1, -1, -1):
            p[sarr[i]].append(i)

        # another pointer to denote the max. sorted index in curr. chunk
        j, ans = -1, 0
        for i in range(n):
            x = arr[i]
            j = max(j, p[x].pop())
            if i < j:
                continue

            # otherwise, we split curr. chunk
            ans += 1
            j = -1

        return ans

arr = [5,4,3,2,1]
arr = [2,1,3,4,4]

Solution().maxChunksToSorted(arr)