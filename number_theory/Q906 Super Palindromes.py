# number theory - hard
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        # key ideas:
        # 1) right bound is up to 1e18, which means there might exists a super-palindrome
        # of magnitude ~1e18 and is a square of a palindrome of magnitude ~1e9
        # 2) given (1), the mirrored left (or right) part of the square root is maximally 5 digits
        # making a linear scan on [1, bound] feasible

        # helper to create palindrome
        def p(base:int, mid:int) -> int:
            if base == 0:
                return 0

            mid_str = str(mid) if mid >= 0 else ''
            return int(str(base) + mid_str + str(base)[::-1])

        # helper to determine if an integer is palindrome
        def is_p(num:int) -> bool:
            s = str(num)
            return s[:(len(s) // 2)] == s[-(len(s) // 2):][::-1]

        # helper to compute # of super-palindromes in range [0, bound]
        def get_sp_cnt(bound:int) -> int:

            if bound <= 0:
                return 1 # [0]
            elif bound <= 3:
                return 2 # [0,1]
            elif bound <= 8:
                return 3 # [0,1,2]
            elif bound <= 9:
                return 4 # [0,1,2,3]

            # explore palindromes with length >= 2
            base, res = 1, 0
            while pow(p(base, -1), 2) <= bound:

                mid = [-1] + list(range(0, 10))
                for x in mid:
                    sp = pow(p(base, x), 2)
                    if sp <= bound and is_p(sp):
                        res += 1

                base += 1

            # account for single-digit super-palindromes
            return res + 4 

        return get_sp_cnt(int(right)) - get_sp_cnt(int(left)-1)
    
left, right = "4", "1000"
left, right = "1", "2"
left, right = "1", str(int(1e18))

Solution().superpalindromesInRange(left, right)