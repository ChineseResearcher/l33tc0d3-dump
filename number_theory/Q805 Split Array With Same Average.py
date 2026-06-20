# number theory - hard
from typing import List
from collections import defaultdict
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1: return False

        # key ideas:
        # 1) suppose the average of entire nums array is A, if we can select k
        # elements from nums s.t. the average of the k elements is A, then it's
        # guaranteed that the other remaining elements also has an average of A.

        # 2) to make the average of k-selection equal to A, where A = sum(nums) / len(nums),
        # it is equivalent to making sure the sum of the k-selection is equal to 
        # k * sum(nums) / len(nums), provided that (k * sum(nums)) % len(nums) = 0

        # 3) we use a "meet-in-the-middle" strategy to first pre-compute the
        # possible subset sums from first / second halve of the nums array.
        # e.g. suppose first halve is [1,2,3,4], then we hash a three-member subset {1,2,3}
        # as {3: [6, ...]} in the hashmap, along with other possible three-member subset sums.

        # 4) to speed things up, we could run a check on whether any group size k in range
        # [1, n-1] could be valid by checking divisibility as mentioned in (2), if there
        # isn't any valid k, we terminate early to judge that it's impossible to split
        S, C = sum(nums), len(nums)

        valid = dict()
        for k in range(1, n):
            if (k * S) % C == 0:
                valid[k] = (k * S) // C

        if not valid: return False

        def get_subset_sum(arr: List[int]) -> dict:

            res = defaultdict(set)
            def dfs(i:int, currSum:int, currCnt:int) -> None:
                if i == len(arr):
                    if currCnt > 0:
                        res[currCnt].add(currSum)
                    return

                # pick / skip
                _ = dfs(i+1, currSum+arr[i], currCnt+1)
                _ = dfs(i+1, currSum, currCnt)
            
            _ = dfs(0, 0, 0)
            return res

        # mid partition + pre-compute
        m = n // 2 
        p1, p2 = get_subset_sum(nums[:m]), get_subset_sum(nums[m:])

        for k in p1.keys():
            for p1_sum in p1[k]:
                if k in valid and p1_sum == valid[k]:
                    return True

                # check if we can find valid complement in the other partition 
                for i in range(k+1, n):
                    if i in valid:
                        if i - k in p2 and valid[i] - p1_sum in p2[i-k]:
                            return True

        return False

nums = [3,1]
nums = [0,0,3,9,8]
nums = [1,2,3,4,5,6,7,8]
nums = [60,30,30,30,30,30,30,30,30,30,30,30,30,30,30]

Solution().splitArraySameAverage(nums)