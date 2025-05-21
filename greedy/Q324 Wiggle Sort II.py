# greedy - medium
from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # this question is tough in the sense that we would need
        # to come up with the correct greedy thinking and apply smartly

        # since wiggle seq. has to be in the form:
        # n1 < n2 > n3 < n4 ....
        # the elements at odd indices should be forward-filled w/ the largest
        # values in reversed order, then fill the even indices

        # to fill the sorted values, first sort nums
        snums = sorted(nums)

        # maintain a pointer to access sorted nums
        idx = n-1

        # fill odd FIRST
        for i in range(1, n, 2):
            
            nums[i] = snums[idx]
            idx -= 1
            
        # fill even
        for j in range(0, n, 2):
            
            nums[j] = snums[idx]
            idx -= 1

        print(nums)

nums = [1,5,1,1,6,4]
nums = [1,3,2,2,3,1]
nums = [4,5,5,6]

Solution().wiggleSort(nums)