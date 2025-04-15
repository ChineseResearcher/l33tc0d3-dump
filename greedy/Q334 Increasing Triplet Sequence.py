# greedy - medium
class Solution:
    def increasingTriplet(self, nums):
        # for triplet problem it's convenient to focus on the middle element
        n = len(nums)

        # build forward min & backward max auxiliary arrays
        forward_min, backward_max = [float('inf')] * n, [float('-inf')] * n

        for i in range(1, n):
            forward_min[i] = min(nums[i-1], forward_min[i-1])
            
        for j in range(n-2, -1, -1):
            backward_max[j] = max(nums[j+1], backward_max[j+1])
            
        for k in range(1, n-1):
            if nums[k] > forward_min[k] and nums[k] < backward_max[k]:
                return True

        return False
    
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]

Solution().increasingTriplet(nums)