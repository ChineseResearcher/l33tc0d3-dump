# array - medium
class Solution:
    def pivotArray(self, nums, pivot):
        n = len(nums)
        # all numbers < pivot are placed to the left and vice versa
        # note that the relative order of elements must be maintained

        # The two-pointers tag is misleading, with two-pointers it has
        # to be modified in-place but looking at discussion that would
        # not be possible without worsening time complexity to O(n^2)

        # process it by building a new auxiliary arr.
        # editorial calls it "O(1) space solution" anyways...
        left, mid, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            if num == pivot:
                mid.append(num)
            if num > pivot:
                right.append(num)

        left.extend(mid)
        left.extend(right)
        return left

nums, pivot = [9,12,5,10,14,3,10], 10
nums, pivot = [-3,4,3,2], 2
nums, pivot = [19,15,12,-14,8,-7,-11], -7

Solution().pivotArray(nums, pivot)