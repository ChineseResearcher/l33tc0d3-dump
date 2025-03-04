# recursion - medium
import math
class Solution:
    def recursiveSum(self, start, currSum):
        
        if currSum == self.n:
            self.ans = True
            return
        
        if currSum > self.n:
            return
        
        for power in range(start, self.maxPower+1):
            self.recursiveSum(power+1, currSum + 3 ** power)

            # early stop
            if self.ans: return

    def checkPowersOfThree(self, n: int) -> bool:
        # as the number is maximally 1e7, i.e. 3 to the power of 14 max.
        # we are trying to explore if some combinations of 3^i for
        # 0 <= i <= 14 would sum up to the number given
        self.maxPower = int(math.log(n, 3))
        self.n = n

        self.ans = False
        self.recursiveSum(0, 0)
        return self.ans

# editorial's solution to solve in O(logN, with base 3)
# the core idea is that for power i of 3
# 3^0 + 3^1 + ... + 3^(i-1) = (3^i - 1)/2 < 3^i
# so if 3^i < n, 3^i has to be part of sum of power3s to n
# as the remaining sum is even smaller
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0

        # Find the largest power that is smaller or equal to n
        while 3**power <= n:
            power += 1

        while n > 0:
            # Subtract current power from n
            if n >= 3**power:
                n -= 3**power
            # We cannot use the same power twice
            if n >= 3**power:
                return False
            # Move to the next lower power
            power -= 1

        # n has reached 0
        return True
    
n = 91
n = 21
# we could do recursion, O(2^N) only because 1e7 is maximally power 14 of 3
# which is the acceptable input size for a recursion algorithm
n = int(1e7 - 1)
n = 4782969
# only the editorial's answer would pass
n = int(1e11 - 1) 

Solution().checkPowersOfThree(n)