# number theory - hard
import math
from collections import Counter
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # edge case: if we have only 1-digit, it is already palindrome by itself
        if n == 1:
            return len([x for x in range(k, 10, k)])

        lo, hi = 10 ** (n // 2 - 1), 10 ** (n // 2)

        N_FAC = math.factorial(n)

        isOdd = (n % 2 != 0)
        # note that for integer x to be called good, it does not have to be
        # divisible by k, only the palindrome form of it does

        def encode(palindrome):
            # given a palindrome string, encode the combination of digits
            # e.g. palindrome = '12021', encode as '011222'
            enc = []
            freq = Counter(list(palindrome))
            for k, v in sorted(freq.items()):
                enc.extend([str(k), str(v)])

            return ''.join(enc)

        k_palindromic, used = set(), set()
        for num in range(lo, hi):

            num_str = str(num)
            # num iterated should be the left half of a palindrome
            if isOdd:
                # odd case we need to test the middle digit too
                for digit in range(0, 10):
                    palindrome = num_str + str(digit) + num_str[::-1]
                    enc = encode(palindrome)

                    if enc not in used and int(palindrome) % k == 0:
                        k_palindromic.add(int(palindrome))
                        used.add(enc)

            else:
                # even case we just test a single palindrome
                palindrome = num_str + num_str[::-1]
                enc = encode(palindrome)

                if enc not in used and int(palindrome) % k == 0:
                    k_palindromic.add(int(palindrome))
                    used.add(enc)

        # we now have obtained the set of k_palindromic numbers
        # in order to count the total good integers we apply combinatorics
        ans = 0
        for num in k_palindromic:

            freq = Counter(list(str(num)))
            # to correctly count the valid rearrangements, we need to
            # not consider cases where it may contain '0' as first digit

            # curr. ans initiated to n!
            curr_ans = N_FAC
            for v in freq.values():
                # applying combinatorics: divide m! for a digit with freq=m
                curr_ans //= math.factorial(v)

            # if '0' is present, remove the cases where it starts with 0
            if '0' in freq:
                
                # permutations after fixing '0' as the first digit
                null_case = math.factorial(n-1)
                # mark used '0'
                freq['0'] -= 1

                for v in freq.values():
                    if v > 0:
                        null_case //= math.factorial(v)

                curr_ans -= null_case
            
            ans += curr_ans

        return ans
    
n, k = 2, 4
n, k = 3, 5
n, k = 5, 6
# test max. n
n, k = 10, 3

Solution().countGoodIntegers(n, k)