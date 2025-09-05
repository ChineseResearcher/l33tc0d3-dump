# bit manipulation - medium
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        # the solving condition essentially requires to let
        # num1 = [pow2_0 + pow2_1 + ... + pow2_k] + k * num2
        # rearranging, [pow2_0 + pow2_1 + ... + pow2_k] = num1 - k * num2

        # generally speaking, for a positive integer "n" w/ "m" set bits
        # to reduce it to 0, we need at LEAST "m" powers of 2
        # e.g. 100 = 0b_01100100 = 2^6 + 2^5 + 2^2, 
        # and at MOST "n" powers of 2, i.e. 100 = 2^0 * 100 in particular

        # it can be proved that for any +ve integer "n" with "m" set bits
        # we can represent "n" using k occurrences of power2 (possibly duplicating powers)
        # given that "m" <= k <= n

        # we thus explore all possible k where num1 can be reduced to 0
        k, ans = 1, -1

        # if curr. k results in non-positive sum of powers of 2,
        # we stop searching as it is impossible for the sum to be non-positive
        while num1 - k * num2 > 0:

            n = num1 - k * num2
            m = bin(n).count('1')
            if m <= k <= n:
                ans = k
                break

            k += 1

        return ans
    
num1, num2 = 3, -2
num1, num2 = 5, 7
num1, num2 = int(1e9), 1 # constraint

Solution().makeTheIntegerZero(num1, num2)