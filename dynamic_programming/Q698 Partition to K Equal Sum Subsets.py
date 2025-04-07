# dp - medium
class Solution:
    def recursive_partition(self, subsetCnt, currSum, avail):

        if subsetCnt == self.k:
            return True if currSum == 0 else False
        
        if (subsetCnt, currSum, avail) in self.dp: 
            return self.dp[(subsetCnt, currSum, avail)]

        currAns = False
        for pos in range(self.n):
            # validate if a pos. is available by accessing bitmask
            if avail & (1 << pos) == 0:
                avail |= (1 << pos)
                currNum = self.nums[self.n-pos-1]
                # we need to consider two scenarios:
                # 1) currNum being added does not exceed target
                # 2) currNum being added exactly equals target, increment subsetCnt
                if currNum + currSum < self.targetNum:
                    currAns = (currAns or self.recursive_partition(subsetCnt, currSum+currNum, avail))
                elif currNum + currSum == self.targetNum:
                    currAns = (currAns or self.recursive_partition(subsetCnt+1, 0, avail))

                # early stop
                if currAns:
                    break

                # backtrack by unsetting bit
                avail &= ~(1 << pos)

        self.dp[(subsetCnt, currSum, avail)] = currAns
        return currAns

    def canPartitionKSubsets(self, nums, k):
        # to form k subsets with equal sum, the total sum must
        # be divisible by k, otherwise stop
        totalSum = sum(nums)
        if totalSum % k != 0: return False

        self.targetNum = totalSum // k

        # another observation is that if any element larger than targetNum, 
        # then it is impossible to have that number in any partition
        if max(nums) > self.targetNum: return False

        # optimisation tricks:
        # 1) for numbers that are exactly equal to targetNum, can be on its own
        # 2) sort filtered nums to reduce recursion depth, as bitmask always access larger num
        temp = []
        for num in nums:
            if num == self.targetNum:
                k -= 1
            else:
                temp.append(num)

        self.nums = sorted(temp)
        self.k = k
        self.n = len(self.nums)

        # it is helpful to encode the available positions
        # at which a num has not been chosen over a bitmask
        bitmask = 0
        self.dp = dict()

        return self.recursive_partition(0, 0, bitmask)
    
nums, k = [4,3,2,3,5,2,1], 4
nums, k = [1,2,3,4], 3
nums, k = [815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], 3

Solution().canPartitionKSubsets(nums, k)