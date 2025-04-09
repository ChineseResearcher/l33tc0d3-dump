# binary search - hard
class Solution:
    def findMin(self, nums):
        n = len(nums)
        # we are given a sorted unique arr. that might have been sorted
        # to find the min. element in O(logN) time, use binary search
        # to locate the idx where nums[idx] > nums[idx+1]

        # edge case 1: length-1 arr.
        # if n == 1: return nums[0]

        # we could binary search on the possible range of rotations
        # note: rotating n times is equivalent to no rotation
        l, r = 1, n-1

        # as compared to the non-duplicate ver., this problem needs
        # two versions of binary search, as the endpoint nums[-1]
        # might be the same as nums[d_idx], e.g. [3,3,3,3,3,3,3,3,1,3]
        # so we would run two vers. to guarantee finding soln if it's really rotated
        def binarySearch(l, r, boundPolicy=1):
            # init. ans to idx 0, assuming it's already sorted and not rotated
            ans = 0
            while l <= r:
                
                rot = (l + r) // 2
                # with k rotations, the decrement should happen at idx n-rot-1
                d_idx = n-rot-1
                # validate decrement
                if nums[d_idx+1] < nums[d_idx]:
                    ans = rot
                    break
                
                # otherwise we could be at the left or right
                # of the actual decrement idx
                else:
                    
                    # determine bound shifts based on left/right
                    if boundPolicy == 1:
                        if nums[d_idx] > nums[-1]:
                            r = rot - 1
                        else:
                            l = rot + 1
                    else:
                        # diff. in sign comparison
                        if nums[d_idx] >= nums[-1]:
                            r = rot - 1
                        else:
                            l = rot + 1

            return ans

        ans = binarySearch(l, r, 1)
        if ans == 0: 
            ans = binarySearch(l, r, 2)

        return nums[n-ans] if ans != 0 else nums[ans]
    
nums = [1,3,5]
nums = [2,2,2,0,1]
nums = [3,3,3,3,3,3,3,3,1,3]

Solution().findMin(nums)