# counting - medium
from typing import List
from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        # notice that the largest number possible for nums[i] is 10^9
        # with the smallest power base of 2, it would breach that limit for 2^32
        # thus, we can say that for any base k, the longest seq. we can have is 
        # k^1, k^2, k^4, k^8, k^16, k^8, k^4, k^2, k^1
        freq = Counter(nums)

        def isValid(num, freq):

            # first test if a number is square-rootable
            numSqrt = int(num ** 0.5)
            if numSqrt ** 2 != num:
                return False
            
            # then test if we have at least 2 occurrences for expand
            # our current desired seq. by length 2
            if freq[numSqrt] < 2:
                return False
            
            return True

        # explore unique numbers and update answer
        ans = 0
        for num in freq.keys():

            # for num = 1, take max possible odd-length
            if num == 1:
                curr_len = freq[num] - 1 if freq[num] % 2 == 0 else freq[num]
                ans = max(curr_len, ans)
                continue

            # treat curr. num as the peak element
            curr_len, curr = 1, num

            while isValid(curr, freq):
                curr_len += 2
                curr = int(curr ** 0.5)

            ans = max(curr_len, ans)

        return ans
    
nums = [5,4,1,2,2]
nums = [1,3,2,4]
nums = [1,1,1,1,1]

Solution().maximumLength(nums)