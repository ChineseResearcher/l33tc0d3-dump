# greedy - medium
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k) -> bool:
        n = len(nums)

        # first rule out the case where nums length is not a multiple of k
        if n // k != int(n / k): return False

        num_freq = Counter(nums)
        num_unique = sorted(Counter(nums).keys())

        # base num is defined to be the starting number 
        # of a group of k consecutive numbers 
        base_num_idx = 0
        while True:

            for i in range(k):
                curr = num_unique[base_num_idx] + i
                if curr not in num_freq:
                    return False
                
                num_freq[curr] -= 1
                if num_freq[curr] == 0: del num_freq[curr]

            # greedily increment the base num
            while num_unique[base_num_idx] not in num_freq:
                base_num_idx += 1

                if base_num_idx == len(num_unique):
                    return True
                
nums, k = [1,2,3,3,4,4,5,6], 4
nums, k = [3,2,1,2,3,4,3,4,5,9,10,11], 3
nums, k = [1,2,3,4], 3
nums, k = [1,2,3,6,7,7], 3

Solution().isPossibleDivide(nums, k)