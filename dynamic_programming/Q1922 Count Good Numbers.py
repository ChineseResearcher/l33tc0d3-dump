# dp - medium
class Solution:
    def recursive_cnt(self, n, isEven):

        if n == 1:
            # if the curr. subproblem is starting at a
            # idx that is not even, it has to be one of the four primes
            return 5 if isEven else 4
        
        if n == 2:
            # there's no need to differentiate the parity 
            # of the starting idx, as both cases contains one odd & even
            return 5 * 4
        
        if (n, isEven) in self.dp: return self.dp[(n, isEven)]

        # the left subproblem inherits the parity directly
        # the right subproblem would depend on the parity of left subproblem
        left_is_even = ((n // 2) % 2 == 0)
        # specifically, if left subproblem is an odd number
        # then the right subproblem would have the opposite state of left
        left = self.recursive_cnt(n // 2, isEven) % self.MOD
        right = self.recursive_cnt(n - n // 2, isEven if left_is_even else not isEven) % self.MOD

        curr = (left * right) % self.MOD
        self.dp[(n, isEven)] = curr
        return curr

    def countGoodNumbers(self, n: int) -> int:
        self.MOD = int(1e9 + 7)
        self.dp = dict()

        return self.recursive_cnt(n, True)
    
n = 1
n = 4
n = int(1e15)

Solution().countGoodNumbers(n)