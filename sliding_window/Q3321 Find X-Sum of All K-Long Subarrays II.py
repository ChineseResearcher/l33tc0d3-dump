# sliding window - hard
from sortedcontainers import SortedSet
from collections import defaultdict
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n = len(nums)
        # key idea: sliding window frequency mapping + two sorted sets
        # as well as a sum tracking sum of elements in topX
        window_freq = defaultdict(int)

        topX = SortedSet() # top X most frequent elements 
        topX_excl = SortedSet(key = lambda x: (-x[0], -x[1])) # remaining

        topX_sum = 0

        # before window slide, process the first k elements
        for i in range(k):
            window_freq[nums[i]] += 1

        for val, f in window_freq.items():
            topX.add((f, val))
            topX_sum += f * val

        # re-balancing
        while len(topX) > x:
            f, val = topX.pop(0)
            topX_excl.add((f, val))
            topX_sum -= f * val

        ans = [topX_sum]
        # now slide the window in range [k, n]
        for r in range(k, n):

            to_add = []
            # deal with the two elements coming into window and out of
            if nums[r] != nums[r-k]:
                for idx in [r, r-k]:

                    val = nums[idx]
                    # prev. freq
                    pf = window_freq[val]
                    # curr. freq
                    if idx == r:
                        window_freq[val] += 1
                    else:
                        window_freq[val] -= 1
                    cf = window_freq[val]

                    length = len(topX)
                    topX.discard((pf, val))
                    # confirmed it was in topX
                    if len(topX) < length:
                        topX_sum -= pf * val
                    # otherwise, it was not in topX
                    else:
                        topX_excl.discard((pf, val))

                    # temporarily store to_add tuple pairs and process later
                    if cf > 0:
                        to_add.append((cf, val))

            for f, val in to_add:
                if not topX_excl:
                    topX.add((f, val))
                    topX_sum += f * val
                    continue

                f1, val1 = topX_excl[0][0], topX_excl[0][1]
                if f > f1 or (f == f1 and val > val1):
                    topX.add((f, val))
                    topX_sum += f * val
                else:
                    topX_excl.add((f, val))

            # re-balancing
            while len(topX) > x:
                f, val = topX.pop(0)
                topX_excl.add((f, val))
                topX_sum -= f * val

            # (reverse) re-balancing
            while topX_excl and len(topX) < x:
                f, val = topX_excl.pop(0)
                topX.add((f, val))
                topX_sum += f * val

            # record answer
            ans.append(topX_sum)

        return ans
    
nums, k, x = [1,1,2,2,3,4,2,3], 6, 2
nums, k, x = [3,8,7,8,7,5], 2, 2
# constraint
nums, k, x = [i for i in range(int(1e5))], 500, 2

Solution().findXSum(nums, k, x)