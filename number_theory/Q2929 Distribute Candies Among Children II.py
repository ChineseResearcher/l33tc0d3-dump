# number theory - medium
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n <= limit:
            return (n+2) * (n+1) // 2

        ans = 0
        for i in range(0, n+1):

            if i > limit:
                break

            # split the problem into m and n-m
            m = n - i

            # test if the problem of m is well-formed for the limit
            if limit < (m / 2):
                continue
            
            # print(m)
            # for the subproblem m, we are trying to distribute m candies
            # to only TWO children while respecting limit for each child
            ans += min(m, limit) - (m - min(m, limit)) + 1

        return ans
    
n, limit = 5, 2
n, limit = 3, 3
n, limit = int(1e6), int(1e6) - 100

Solution().distributeCandies(n, limit)