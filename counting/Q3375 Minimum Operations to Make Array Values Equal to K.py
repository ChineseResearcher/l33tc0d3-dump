# counting - easy
from collections import Counter
class Solution:
    def minOperations(self, nums, k):
        
        # the valid integer h is only going to be reduced, and we want
        # to see if h can be reduced to match k

        # thus if the minimum of nums if smaller than k, there's no way
        # for us to make an integer h equal to k as it is already smaller
        minN, maxN = min(nums), max(nums)

        if minN < k: return -1

        # e.g. we have nums = [2,2,2] and k = 1, only 1 operation needed
        if minN == maxN: return 1 if minN > k else 0

        freq = Counter(nums)

        ops_cnt = 0
        for num in range(maxN-1, minN-1, -1):
            
            if freq[num] > 0:
                # simulate reduction of h to num
                ops_cnt += 1
                
        ops_cnt += 1 if minN > k else 0
        return ops_cnt
    
nums, k = [5,2,5,4,5], 2
nums, k = [2,1,2], 2
nums, k = [9,7,5,3], 1

Solution().minOperations(nums, k)