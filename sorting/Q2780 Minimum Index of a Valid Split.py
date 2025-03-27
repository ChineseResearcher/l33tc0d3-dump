from collections import Counter
class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
        # freq. count of numbers
        num_freq = Counter(nums)

        # the proof of correctness in choosing the number with max. freq
        # as the dominant number to scan for is not so straightforward
        max_num, max_num_freq = sorted(num_freq.items(), key=lambda item: item[1], reverse=True)[0]

        freq_left, ans = 0, -1
        # valid partition from left <= 0 to left <= n-2
        for i in range(n-1):

            if nums[i] == max_num:
                freq_left += 1

            freq_right = max_num_freq - freq_left
            if freq_left * 2 > (i+1) and freq_right * 2 > (n-i-1):
                ans = i
                break

        return ans
    
nums = [2,1,3,1,1,1,7,1,2,1]
nums = [1,2,2,2]
nums = [3,3,3,3,7,2,2]

Solution().minimumIndex(nums)