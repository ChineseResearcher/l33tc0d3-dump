# number theory - medium
class Solution:
    def isPrime(self, num):
        # check if a number is prime provided 1 < num < inf
        searchRange = [2] + list(range(3, int(num**0.5+1), 2))
        for divisor in searchRange:
            if num != divisor and num % divisor == 0:
                return False

        return True

    def primeSubOperation(self, nums) -> bool:
        # pad a 0 to the start of nums
        nums = [0] + nums

        n = len(nums)
        for i in range(1, n):

            currOptPrime = None
            # smallest prime to subtract is 2, so lower bound = 1
            for j in range(nums[i]-nums[i-1]-1, 1, -1):
                if self.isPrime(j):
                    currOptPrime = j
                    break

            if currOptPrime is None:
                if i < n-1 and (nums[i] >= nums[i+1] or nums[i] <= nums[i-1]):
                    return False
                if i == n-1 and nums[i] <= nums[i-1]:
                    return False

            if currOptPrime is not None:
                # print(f'subtracting {currOptPrime}')
                nums[i] -= currOptPrime

        return True
    
nums = [4,9,6,10]
nums = [6,8,11,12]
nums = [5,8,3]
nums = [1,20,7,12,4]
nums = [11,2,10,15,19]

Solution().primeSubOperation(nums)