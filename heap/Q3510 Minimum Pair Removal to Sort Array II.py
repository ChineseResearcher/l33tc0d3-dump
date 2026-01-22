# heap - hard
import heapq
from typing import List
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        n = len(nums)
        # key ideas
        # 1) use two hashmaps prev/next to build the neighbour relationships

        # 2) maintain an array called removed, default to False. When a pair
        # is merged, the larger index gets "removed" and turned True

        # 3) use a minheap to always query the min. pairsum, break even by index
        # i.e. minheap stores <pairSum, i, j> where (i,j) is the pair of indices

        # 4) how do we know in O(1) time in each iteration that curr. underlying
        # array is already non-descending? we first record all indices s.t. there's
        # a smaller relationship in a set and perform deletion on this set until empty

        removed = [False] * n
        prev, next = dict(), dict()
        minheap = []
        val = [] # init. to nums, gets dynamically updated

        smaller = set()
        for i in range(n):
            if i > 0:
                if nums[i] < nums[i-1]:
                    smaller.add(i)
                heapq.heappush(minheap, (nums[i-1]+nums[i], i-1, i))

            prev[i] = i-1 if i-1 >= 0 else -1
            next[i] = i+1 if i+1 <= n-1 else -1
            val.append(nums[i])

        if not smaller:
            return 0

        ans = 0
        while minheap:

            pairSum, i, j = heapq.heappop(minheap)
            # skip invalid cases
            # case 1: either i or j already in removed
            if removed[i] or removed[j]:
                continue
            # case 2: pairSum is outdated
            if val[i] + val[j] != pairSum:
                continue

            # mark j as removed
            removed[j] = True
            # override val at index i w/ pairSum
            val[i] = pairSum
            # override next neighbour of i with that of j
            next[i] = next[j]
            # override prev neighbour of j's next to i
            prev[next[j]] = i
            # introduce new candidates to minheap
            if prev[i] != -1:
                heapq.heappush(minheap, (val[prev[i]]+val[i], prev[i], i))
            if next[i] != -1:
                heapq.heappush(minheap, (val[i]+val[next[i]], i, next[i]))

            ans += 1
            # validate nonDesc property
            smaller.discard(j)
            
            if prev[i] != -1:
                if val[i] >= val[prev[i]]:
                    smaller.discard(i)
                else:
                    smaller.add(i)

            if next[i] != -1:
                if val[i] <= val[next[i]]:
                    smaller.discard(next[i])
                else:
                    smaller.add(next[i])

            if not smaller:
                break

        return ans
    
nums = [1,2,2]
nums = [5,2,3,1]
nums = [0,-1,-1,-1,1,0,-1]
nums = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]

Solution().minimumPairRemoval(nums)