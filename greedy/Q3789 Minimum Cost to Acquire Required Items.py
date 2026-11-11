# greedy - medium
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) use type3 @ costBoth throughout if it's the minimum
        # 2) greedily use type3 @ costBoth if costBoth <= cost1 + cost2, and satisfy
        # the remaining w/ either min(type1/2, type3)

        if costBoth <= cost1 and costBoth <= cost2:
            return max(need1, need2) * costBoth

        if costBoth <= cost1 + cost2:
            ans = fmin(need1, need2) * costBoth
            if need1 > need2:
                ans += (need1 - need2) * fmin(cost1, costBoth)
            else:
                ans += (need2 - need1) * fmin(cost2, costBoth)
            return ans

        # otherwise, we fulfil w/ only type1 and type2
        return need1 * cost1 + need2 * cost2

cost1, cost2, costBoth, need1, need2 = 3, 2, 1, 3, 2
cost1, cost2, costBoth, need1, need2 = 5, 4, 15, 2, 3
cost1, cost2, costBoth, need1, need2 = 5, 4, 15, 0, 0
cost1, cost2, costBoth, need1, need2 = 37, 53, 45, 5, 18

Solution().minimumCost(cost1, cost2, costBoth, need1, need2)