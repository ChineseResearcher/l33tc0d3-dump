# sliding window - medium
from collections import defaultdict
class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        
        # keep expanding window's right end if the total number of pairs
        # fall short of k, and contract window's left end once reached
        window_freq, window_pairs = defaultdict(int), 0

        l, ans = 0, 0
        for r in range(n):
            
            curr = nums[r]
                
            curr_freq = window_freq[curr]
            if curr_freq > 1:
                # discount window_pairs by nC2
                window_pairs -= curr_freq * (curr_freq - 1) // 2

            window_freq[curr] += 1
            curr_freq = window_freq[curr]
            if curr_freq > 1:
                window_pairs += curr_freq * (curr_freq - 1) // 2
                    
            if window_pairs >= k: 
            
                # window shrinking
                while True:

                    temp = window_pairs
                    # test deletion of nums[l]
                    curr_freq = window_freq[nums[l]]
                    if curr_freq > 1:
                        temp -= curr_freq * (curr_freq - 1) // 2

                    curr_freq -= 1
                    if curr_freq > 1:
                        temp += curr_freq * (curr_freq - 1) // 2

                    if temp < k:
                        break

                    # otherwise we are good to shrink left
                    window_pairs = temp
                    window_freq[nums[l]] = curr_freq
                    l += 1
                
                # ans incremented base on pos of left pointer
                ans += l+1
                 
        return ans
    
nums, k = [1,1,1,1,1], 10
nums, k = [3,1,4,3,2,2,4], 2
nums, k = [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], 11

Solution().countGood(nums, k)