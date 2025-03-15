# binary search - medium
class Solution:
    def canRob(self, nums, target, k):
        # given a targeted miniMax (minimum capability), test if
        # we could form a group with at least k members with max(group) being the target

        # init. the index of last robbed house to -2 so that it is not a neighbour of index 0
        lastRobbed = -2
        
        cnt = 0
        # count number of houses robbed s.t. no consecutive houses are robbed 
        for i in range(len(nums)):
            if nums[i] <= target and i > lastRobbed + 1:
                cnt += 1
                lastRobbed = i

        return True if cnt >= k else False

    def minCapability(self, nums, k):
        # the phrasing of this question is confusing, but the gist is
        # to find the miniMax of a group of elements of size k, subject
        # to the cond. that each element is at least one index apart from
        # the nearest element in the group. 

        # e.g. the miniMax solution for: nums=[2,3,5,9], k = 2 is the group
        # [2,_,5,_] and 5 is is the max. of the group, thus the ans

        # edge case: k being 1 means the min. of nums can be a group by itself
        if k == 1: return min(nums)

        unique = sorted(set(nums))
        l, r = 0, len(unique) - 1

        ans = unique[-1]
        while l <= r:

            mid = (l+r) // 2
            if self.canRob(nums, unique[mid], k):
                ans = min(ans, unique[mid])
                r = mid - 1

            else:
                l = mid + 1

        return ans
    
nums, k = [2,3,5,9], 2
nums, k = [2,7,9,3,1], 2
nums, k = [35,9,18,78,40,8,71,2,59], 5

Solution().minCapability(nums, k)