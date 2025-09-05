# bit manipulation - medium
from typing import List
class Solution:
    def printInBinary(self, num, bit_length=34):
        bit_str = "{0:b}".format(num & (2**bit_length -1))
        bit_str = "0"*(bit_length-len(bit_str)) + bit_str
        return bit_str

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l, n = 0, len(nums)
        ans = float('inf')
        cumu_OR = 0

        bit_freq = [0 for _ in range(34)]
        for r in range(n):

            if nums[r] >= k:
                return 1

            cumu_OR = cumu_OR | nums[r]
            for idx, bit in enumerate(self.printInBinary(nums[r])):
                if bit == '1':
                    bit_freq[idx] += 1

            if cumu_OR >= k:
                ans = min(ans, r-l+1)

                while True:

                    temp, temp_str = [], self.printInBinary(nums[l])
                    for idx, bit in enumerate(temp_str):
                        if bit == '1':
                            bit_freq[idx] -= 1

                        if bit_freq[idx] > 0:
                            temp.append('1')
                        else:
                            temp.append('0')
                    
                    temp_OR = int(''.join(temp), 2)
                    if temp_OR >= k:
                        l += 1
                        ans = min(ans, r-l+1)
                        cumu_OR = temp_OR
                    else:
                        # undo the decrementing on counter
                        for idx, bit in enumerate(temp_str):
                            if bit == '1':
                                bit_freq[idx] += 1
                        break
            
        return ans if ans < float('inf') else -1
    
nums, k = [1,2,3], 2
nums, k = [2,1,8], 10
nums, k = [1,2], 0
nums, k = [2,1,9,12], 21

Solution().minimumSubarrayLength(nums, k)