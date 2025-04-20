# sliding window - medium
class Solution:
    def numberOfSubarrays(self, nums, k) -> int:

        subarrayOddCount = 0
        ans = 0
        leftPointer = 0
        n = len(nums)

        for i in range(n):

            if nums[i] % 2 == 1:
                subarrayOddCount += 1

                if subarrayOddCount == k:
                    
                    rightPointer = i + 1
                    leftCount, rightCount = 1, 1
                    while nums[leftPointer] % 2 == 0:
                        leftPointer += 1
                        leftCount += 1

                    while rightPointer < n and nums[rightPointer] % 2 == 0:
                        rightPointer += 1
                        rightCount += 1

                    ans += leftCount * rightCount
                    subarrayOddCount -= 1
                    leftPointer += 1

        return ans
    
nums, k = [1,1,2,1,1], 3
nums, k = [2,4,6], 1
nums, k = [2,2,2,1,2,2,1,2,2,2], 2

Solution().numberOfSubarrays(nums, k)