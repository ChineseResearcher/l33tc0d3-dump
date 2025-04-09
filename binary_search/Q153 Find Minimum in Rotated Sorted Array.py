# binary search - medium
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
                if nums[d_idx] > nums[-1]:
                    r = rot - 1
                else:
                    l = rot + 1
                    
        if ans != 0:
            return nums[n-ans]
        else:
            return nums[ans]
        
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]

Solution().findMin(nums)