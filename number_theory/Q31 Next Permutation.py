# number theory - medium
from typing import List
class Solution:
    def swap(self, swap_i, swap_j):
    
        temp = self.nums[swap_j]
        self.nums[swap_j] = self.nums[swap_i]
        self.nums[swap_i] = temp

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using sorted(list(itertools.permutations(arr))) to generate all possible unique combinations,
        # we can notice that the next-in-order combination requires us to swap the latest pair
        # of indices such that arr[i] < arr[j] for j > i

        n = len(nums)
        self.nums = nums
        swap_i, swap_j = None, None
        for i in range(n-1):
            for j in range(i+1, n):
                if self.nums[j] > self.nums[i]:
                    swap_i, swap_j = i, j

        if swap_i is None and swap_j is None:
            swap_i, swap_j = 0, n-1
        
        self.swap(swap_i, swap_j)

        for i in range(swap_i+1, n-1):
            for j in range(i+1, n):

                if self.nums[j] < self.nums[i]:
                    self.swap(i, j)

nums = [1,2,3]
nums = [3,2,1]
nums = [1,1,5]
nums = [1,3,2]

Solution().nextPermutation(nums)