# binary search - medium
class Solution:
    def canDistribute(self, arr, n, k):

        # important to note that a child cannot be receiving candies
        # from more than one original pile in candies arr.

        # however a pile in candies arr. can be subdivided to serve
        # more than one child, e.g. candies = [5,8,6], k = 5
        # we can serve each child 3 candies if we break down our
        # piles s.t. 5 (one pile), 8 (two piles), 6 (two piles)

        for pile in arr:
            k -= pile // n
            if k <= 0: return True

        return False

    def maximumCandies(self, candies, k):
        
        # binary search on max. possible "n" candies that each child could get
        l, r = 1, max(candies)
        ans = 0

        while l <= r:

            n = (l + r) // 2
            if self.canDistribute(candies, n, k):
                ans = max(ans, n)
                # greedily search for larger n
                l = n + 1
            else:
                r = n - 1

        return ans
    
candies, k = [5,8,6], 3
candies, k = [5,8,6], 5
candies, k = [2,5], 11

Solution().maximumCandies(candies, k)