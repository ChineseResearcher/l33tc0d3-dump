# bit manipulation - easy
from collections import defaultdict
import math
class Solution:
    def xor_backtrack(self, curr_xor, curr_idx):

        self.subset_xor.append(curr_xor)

        for i in range(curr_idx, len(self.nums)):
            curr_xor ^= self.nums[i]
            self.xor_backtrack(curr_xor, i+1)
            # backtrack by performing xor with nums[i] again
            curr_xor ^= self.nums[i]

    def subsetXORSum(self, nums):
        self.nums = nums
        # note that:
        # 1) a subset need not be contiguous block of nums
        # 2) for n numbers, there are 2^n subset

        self.subset_xor = []
        self.xor_backtrack(0, 0)

        # additional analysis on setbit frequencies
        # setbit_freq stores <idx from right end, freq of set bit>
        setbit_freq = defaultdict(int)

        # define max_set_bit as the largest set bit pos. possible
        max_set_bit = int(math.log(20) / math.log(2))

        for xor_res in self.subset_xor:

            bit_pos = 0
            while bit_pos <= max_set_bit:
                # indicate set bit
                if xor_res & (1 << bit_pos) != 0:
                    setbit_freq[bit_pos] += 1

                bit_pos += 1

        print(f'for {len(self.subset_xor)} subsets, each set bit appears with following frequency:')
        print(setbit_freq)

        return sum(self.subset_xor)
    
class Solution:
    def subsetXORSum(self, nums):
        # from editorial & forum:
        # this problem can be solved by bruteforce using backtracking
        # but there exists O(N) solution using purely bit manipulation

        # from my brute force soln above, it can be shown that:
        # As long as the i-th bit is set in any number of an array, 
        # that bit will be set exactly 2^(n-1) times in the subsets of the array

        # the O(N) approach first perform bitwise OR to obtain all possible setbits
        # then it can be proven that the subset XOR sum is the bitwise OR * 2^(n-1)
        or_all = 0

        for num in nums:
            or_all |= num

        return or_all * (2 ** (len(nums) - 1))
    
nums = [1,3]
nums = [5,1,6]
nums = [3,4,5,6,7,8]

Solution().subsetXORSum(nums)