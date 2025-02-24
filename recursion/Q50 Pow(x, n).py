# recursion - medium
class Solution:
    def recursivePow(self, x, n):
        intN = int(n)
        if intN == 0:
            return 1
        # recursive call with power halved
        powerHalved = self.recursivePow(x, n/2)

        if intN % 2 == 0:
            return powerHalved * powerHalved
        else:
            if n >= 0:
                return powerHalved * powerHalved * x
            else:
                # handle negative power
                return powerHalved * powerHalved * (1/x)

    def myPow(self, x: float, n: int) -> float:
        # thinking of this problem recursively results in O(logN) complexity
        # this is faster than a linear product sum of x for n times
        return self.recursivePow(x, n)
    
x, n = 2.00000, 10
x, n = 2.10000, 3
x, n = 2.00000, -2

Solution().myPow(x, n)