# array - easy
class Solution:
    # O(n^2) would pass, but implemented in O(n) as a challenge
    def check(self, nums) -> bool:
        # if nums was able to result in the sorted ver. of itself
        # then it follows a v-shape if we could start at some index i and rotate

        # let the first element be the smallest element
        cap = nums[0]

        # record the index at which the first decrement happens
        # at most 100 elements, so dummy to 101 to indicate unassigned
        decremented = 101 
        for i in range(1, len(nums)):

            # two decrements would not lead to desired sorted ver.
            # e.g. [8,5,3]
            if i > decremented and nums[i] < nums[i-1]:
                return False

            if nums[i] < nums[i-1]:
                decremented = i

            if decremented != 101 and nums[i] > cap:
                return False

        return True
    
nums = [3,4,5,1,2]
nums = [2,1,3,4]
nums = [1,2,3]
nums = [1,1,1,2] # there can be duplicates
nums = [1,2,1,1]
nums = [8,5,4,5,1,4,5,2,2]

Solution().check(nums)
