# number theory - medium
class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n < 2: return 0

        def cnt_2_or_5(ub):
            # a helper function to calculate for the range
            # [1, ub], what's the cnt of 2 and 5 appearing as prime factors
            # e.g. 20 = 2^2 * 5, so we return (2, 1)
            two_cnt, five_cnt = 0, 0
            
            for num in range(1, ub+1):
                while num > 0 and num % 2 == 0:
                    two_cnt += 1
                    num //= 2
                    
                while num > 0 and num % 5 == 0:
                    five_cnt += 1
                    num //= 5
                    
            return two_cnt, five_cnt
        
        # the mathemtical reasoning behind is that to have trailling zeros
        # we need to have 10 as an intermediary product for every zero appearing
        # e.g. in 5!, where 5! = 5 x 4 x 3 x 2 x 1, we can re-arrange into
        # (5 x 2) x 4 x 3 x 1 = 10 x 4 x 3 x 1, where one occurrence of 10
        # contributes to exactly one trailling zero for factorial of 5.

        # the occurrences of product 10 is bounded by the occurrences of 2 and 5
        # and whichever is lower gives us the answer
        return min(cnt_2_or_5(n))
    
n = 3
n = 5
n = int(1e4)

Solution().trailingZeroes(n)