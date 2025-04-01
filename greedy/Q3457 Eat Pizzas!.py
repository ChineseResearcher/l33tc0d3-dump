# greedy - medium
class Solution:
    def maxWeight(self, pizzas):
        n = len(pizzas)
        # we are given n that is multiple of 4, and we eat 4 pizzas per day
        # goal is to find max. total weight after n // 4 days

        days = n // 4
        # on odd-days (1-indexed) we gain max(p1, p2, p3, p4) weight
        # so we should always process odd-days first, this is the greedy thinking
        pizzas.sort()

        ans = 0
        # process odd-days
        for _ in range(1, days+1, 2):
            ans += pizzas.pop()

        # porcess even-days
        for _ in range(2, days+1, 2):
            # on even-days we gain second largest weight
            pizzas.pop()
            ans += pizzas.pop()

        return ans
    
pizzas = [1,2,3,4,5,6,7,8]
pizzas = [2,1,1,1,1,1,1,1]

Solution().maxWeight(pizzas)