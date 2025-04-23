# number theory - easy
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_grp, ans = 0, 0

        grp_size = defaultdict(int)
        for i in range(1, n+1):

            # to very efficiently compute the digitSum,
            # we use divMod where it returns both quotient and remainder
            digitSum, num = 0, i
            while num > 0:
            
                q, r = divmod(num, 10)
                digitSum += r
                num = q

            grp_size[digitSum] += 1

            # track ans
            if grp_size[digitSum] == max_grp:
                ans += 1
            elif grp_size[digitSum] > max_grp:
                max_grp = grp_size[digitSum]
                ans = 1

        return ans
    
n = 2
n = 13
n = 9999

Solution().countLargestGroup(n)