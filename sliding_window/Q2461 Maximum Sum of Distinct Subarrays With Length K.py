# sliding window - medium
from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        # use a dict to track the element frequency in a window of size k
        window_freq, window_sum = Counter(nums[:k]), sum(nums[:k])
        invalid = set([k for k,v in window_freq.items() if v > 1])

        ans = window_sum if len(invalid) == 0 else 0
        for i in range(k, n):

            to_add, to_del = nums[i], nums[i-k]
            window_sum += to_add
            window_sum -= to_del

            if to_add not in window_freq:
                window_freq[to_add] = 1
            else:
                window_freq[to_add] += 1
                invalid.add(to_add)

            window_freq[to_del] -= 1
            if window_freq[to_del] == 1:
                # falls back into unique status, remove from invalid
                invalid.discard(to_del)
            if window_freq[to_del] == 0:
                del window_freq[to_del]
            
            if len(invalid) == 0:
                ans = max(ans, window_sum)

        return ans
    
nums, k = [1,5,4,2,9,9,9], 3
nums, k = [4,4,4], 3

Solution().maximumSubarraySum(nums, k)