# greedy - medium
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        # key ideas:
        # 1) greedily pick the largest two piles if non-empty at each step
        # 2) as there are only 3 variables, simply sort at each iteration
        p = [a, b, c]

        ans = 0
        while True:

            p.sort()
            if p[-1] > 0 and p[-2] > 0:
                ans += 1
                p[-1] -= 1
                p[-2] -= 1
            else:
                break

        return ans
    
a, b, c = 2, 4, 6
a, b, c = 4, 4, 6
a, b, c = 1, 8, 8

Solution().maximumScore(a, b, c)