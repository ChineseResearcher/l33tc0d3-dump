# number theory - medium
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) simulation of making even or odd
        # 2) when making even, if curr. nums1[i] is odd, we need to find a smaller odd
        #    when making odd, if curr. nums1[i] is even, we also need to find a smaller odd
        # 3) pre-process the array to find the smallest odd and even (if any)
        o_0, e_0 = float('inf'), float('inf')

        for x in nums1:
            if x % 2 == 1:
                o_0 = fmin(o_0, x)
            else:
                e_0 = fmin(e_0, x)

        # impossible to make an even nums2 if an odd nums[i] is present
        make_even = False if o_0 < float('inf') else True

        # impossible to make an odd nums2 if the smallest even nums[i] < smallest odd nums[i]
        make_odd = False if e_0 < o_0 else True

        return make_even or make_odd

nums1 = [2,3]
nums1 = [4,6]
nums1 = [1,4,7]

Solution().uniformArray(nums1)