# binary search - easy
class Solution:
    def maximumCount(self, nums) -> int:
        n = len(nums)
        # we are given a nums arr. sorted in increasing order
        # it is helpful to use binary search to locate the first neg/pos number

        # find first pos
        l, r = 0, n-1
        first_pos = n
        while l <= r:

            mid = (l + r) // 2
            if nums[mid] > 0:
                first_pos = min(first_pos, mid)
                r = mid - 1
            else:
                l = mid + 1

        # find first neg
        l, r = 0, n-1
        first_neg = -1
        while l <= r:

            mid = (l+r) // 2
            if nums[mid] < 0:
                first_neg = max(first_neg, mid)
                l = mid + 1
            else:
                r = mid - 1

        return max(first_neg-(-1), n-first_pos)
    
nums = [-2,-1,-1,1,2,3]
nums = [-3,-2,-1,0,0,1,2]
nums = [5,20,66,1314]

Solution().maximumCount(nums)