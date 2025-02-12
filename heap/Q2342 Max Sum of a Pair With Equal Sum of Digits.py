# heap - medium
import heapq
class Solution:
    def maximumSum(self, nums):

        digitSum = dict()
        validSum = set()

        for num in nums:

            # find the digit sum of the curr number
            # where a number is maximally 1e9 / 10^9
            currSum = sum([int(x) for x in list(str(num))])

            if currSum not in digitSum:
                digitSum[currSum] = []

            # maintain a max-heap
            heapq.heappush(digitSum[currSum], -num)

            # we are only interested in digitSum pairs
            # so at least occur twice to update our maxSum
            if len(digitSum[currSum]) > 1:
                validSum.add(currSum)

        ans = -1
        for s in validSum:

            pairSum = 0
            # get the two max. numbers that gave rise to a digitSum
            for _ in range(2):
                pairSum += abs(heapq.heappop(digitSum[s]))

            if pairSum > 0: ans = max(ans, pairSum)

        return ans
    
nums = [10,12,19,14]
nums = [18,43,36,13,7]
nums = [368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]

Solution().maximumSum(nums)