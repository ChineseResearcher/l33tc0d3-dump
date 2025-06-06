# number theory - hard
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # given any target n, the longest length of a consecutive seq.
        # that would sum to n would not exceed 2 * (sqrt(n)) by observation

        maxLen = int(2 * int(n ** 0.5))
        # then we can explore every possible length k, and determine if 
        # n can be a sum of k consecutive integers

        def canSumToN(N, l):
            # helper to determine if "l" consecutive numbers sum to N in O(1)
            # note that we need the formula:
            # (a + a + l) * (l + 1) / 2 = n
            
            # w/ some algebra, we formulate
            # a = (2*n - l^2 - len) / (2*l + 2) iff there's valid "a"

            numerator = 2*N - l**2 - l
            if numerator <= 0:
                return False
            
            denominator = 2*l + 2
            return True if numerator % denominator == 0 else False

        # ans init. to 1 because n itself form n
        ans = 1 
        for k in range(2, maxLen+1):

            if canSumToN(n, k-1):
                ans += 1

        return ans
    
n = 3
n = 5
n = 9
n = 15
n = int(1e9)

Solution().consecutiveNumbersSum(n)