# prefix sum - medium
class Solution:
    def subarraySum(self, nums, k):
        prefix_dict = {0:1} # handle case where a subarr in the form of nums[:i] sums to k
        currSum = 0
        subArrEqualKCnt = 0
        for i, num in enumerate(nums):

            currSum += num
            target = currSum - k
            if target in prefix_dict:
                subArrEqualKCnt += prefix_dict[target]
            
            # increment the occurrence count of currSum by 1 if exists else initiate to 1
            if currSum in prefix_dict:
                prefix_dict[currSum] += 1
            else:
                prefix_dict[currSum] = 1

        return subArrEqualKCnt
    
nums, k = [1,1,1], 2
nums, k = [1,2,3], 3
nums, k = [-1,-1,1], 0
nums, k = [1,-1,0], 0
nums, k = [1], 1

Solution().subarraySum(nums, k)