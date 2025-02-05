# monotonic stack - medium
class Solution:
    def nextGreaterElements(self, nums):
        # since we are having a circular array for next greater element
        # it would be convenient for us to simply multiply the nums arr by 2

        n = len(nums)
        ans = nums[:]

        nums = nums * 2

        # to achieve O(n) time we apply the concept of monotonic stack
        # which stores indices of elements which has not yet found a greater element
        replaceIdx = []

        for i, num in enumerate(nums):

            while replaceIdx and ans[replaceIdx[-1]] < num:
                idx = replaceIdx.pop()
                
                if idx < n:
                    ans[idx] = num

            # we are only concerned about indices falling in the range
            # of the original nums array: 0 -> n-1
            if i < n:
                replaceIdx.append(i)

        # handle unreplaced indices
        for x in replaceIdx:
            ans[x] = -1

        return ans
    
nums = [1,2,1]
nums = [1,2,3,4,3]

Solution().nextGreaterElements(nums)