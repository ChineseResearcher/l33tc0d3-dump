# dp - hard
from functools import cache
from string import ascii_lowercase as lwc
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        n = len(s)

        @cache
        def recursive_op(i: int, wildcard: bool, usage: int) -> int:

            # i: where we are in string s
            # wildcard: boolean to indicate if we've used replacement
            # usage: bitmask to indicate the usage of 26 alphabets
            if i == n:
                return 1 if usage != 0 else 0
            
            curr_res = 0
            for char in lwc:

                if char != s[i] and wildcard:
                    continue

                # then we execute the following where:
                # 1) char is same as s[i]
                # 2) char is diff. from s[i] but wildcard is available

                # add curr. char to usage
                nu = usage
                nu |= (1 << (ord(char) - ord('a')))

                # update wildcard status
                nw = wildcard
                nw |= (char != s[i])

                # if by adding this char we have breached k
                # we need to create a partition ending before s[i]
                if nu.bit_count() > k:
                    
                    # reset usage
                    nu = 1 << (ord(char) - ord('a'))
                    n_res = 1 + recursive_op(i+1, nw, nu)

                else:
                    n_res = recursive_op(i+1, nw, nu)

                if n_res > curr_res:
                    curr_res = n_res

            return curr_res

        return recursive_op(0, False, 0)
    
s, k = "accca", 2
s, k = "aabaab", 3
s, k = "xxyz", 1

Solution().maxPartitionsAfterOperations(s, k)