# prefix sum - medium
class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1
        
        return count
    
nums, k = [4,5,0,-2,-3,1], 5
nums, k = [5], 9

Solution().subarraysDivByK(nums, k)