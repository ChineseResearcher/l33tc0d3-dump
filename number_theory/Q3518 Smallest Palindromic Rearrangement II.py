# number theory - hard
from collections import Counter
# pre-compute factorials up to m
fac = [0] * 5001
fac[0] = 1
for i in range(1, 5001):
    fac[i] = i * fac[i-1]

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        n = len(s)
        if n == 1: return s if k == 1 else ''
        
        # key ideas:
        # 1) observe that there could be only UP TO 1 char. w/ cnt being odd,
        # otherwise, the palindrome given is not valid
        # 2) build the first halve of the final string by using the original
        # frequencies of each unique char. floor-divided by 2
        # 3) we do not need to simulate lexicographically ordered patterns
        # one by one, we can speed up using combinatorics
        m = n // 2

        mid, freq = [], Counter(s)
        for c, f in freq.items():
            if f % 2 == 1:
                mid.append(c)
            freq[c] //= 2

        total = fac[m]
        for f in freq.values():
            total //= fac[f]

        # reject invalid (larger) k
        if k > total: return ''

        # get sorted unique chars. to simulate lexicographically
        c_list = sorted(freq.keys())

        # keep incrementing prefix count until it exceeds target "k"
        halve, pf_cnt = [], 0

        while len(halve) < m:

            # define "r" as the remaining number of positions to fill
            # as suffix after placing a char. at curr. index
            r = m - len(halve)

            for c in c_list:
                if freq[c] > 0:
                    # for [0,...,i,i+1,...n-1], if we set halve[i] to c
                    # we can compute variations in range [i+1, n-1] directly

                    # to optimize the computation of variations, we need to observe:
                    # total = r! // (c1! * c2! * ... * ci!)
                    # and by placing another char. "c", we would have suffix
                    # variations equal to (r - 1)! // (c1! * c2! * (cX-1)! * ... * ci!)
                    # where cX refers to freq[c], and we consume one count to have cX - 1.
                    # Then, rewrite total as:
                    # r * (r - 1)! // (cX * c1! * c2! * (cX-1)! * ... * ci!)
                    # which is equivalent to: 
                    # total = r / cX * suffix_variations 
                    # OR suffix_variations = total * cX / r
                    cX = freq[c]

                    suffix_var = total * cX // r
                    # add curr. char. as the prefix if prefix count exceeds target
                    if pf_cnt + suffix_var >= k:
                        halve.append(c)
                        freq[c] -= 1
                        total = suffix_var
                        break
                    # search further at curr. index
                    pf_cnt += suffix_var

        return ''.join(halve + mid + halve[::-1])

s, k = "aa", 2
s, k = "abba", 2
s, k = "bacab", 1
s, k = "abbcbba", 3

Solution().smallestPalindrome(s, k)