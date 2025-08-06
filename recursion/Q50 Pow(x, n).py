# recursion - medium
from functools import cache
class Solution:
    @cache
    def recursivePow(self, x, n):

        if n == 0:
            return 1
        
        if n >= 0:
            nn = n // 2
        else:
            nn = -(abs(n) // 2)

        # recursive call with power halved
        powerHalved = self.recursivePow(x, nn)

        if abs(n) % 2 == 0:
            return powerHalved * powerHalved
        else:
            if n >= 0:
                return powerHalved * powerHalved * x
            else:
                # handle negative power
                return powerHalved * powerHalved * (1 / x)

    def myPow(self, x: float, n: int) -> float:

        # core ideas:
        # 1) tackling this problem recursively results in O(logN) complexity
        # 2) as we might repeat subproblems, speed up using cache
        return self.recursivePow(x, n)
    
x, n = 2.00000, 10
x, n = 2.10000, 3
x, n = 2.00000, -2

Solution().myPow(x, n)