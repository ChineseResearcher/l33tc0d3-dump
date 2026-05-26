# prefix sum - medium
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        n = len(nums)
        # key ideas:
        # 1) first prepare closest(x) arr. for every index x
        # 2) we build prefix / suffix cumulative costs based on above array

        clo = [float('inf')] * n
        clo[0] = 1
        clo[-1] = n-2
        for i in range(1, n-1):
            
            l_diff = nums[i] - nums[i-1]
            r_diff = nums[i+1] - nums[i]
            if l_diff <= r_diff:
                clo[i] = i-1
            else:
                clo[i] = i+1

        # prefix
        pf_cost, cumu_cost = [0], 0
        for i in range(1, n):

            if clo[i-1] == i:
                cumu_cost += 1
            else:
                cumu_cost += nums[i] - nums[i-1]

            pf_cost.append(cumu_cost)

        # suffix
        sf_cost, cumu_cost = [0], 0
        for i in range(n-2, -1, -1):

            if clo[i+1] == i:
                cumu_cost += 1
            else:
                cumu_cost += nums[i+1] - nums[i]

            sf_cost.append(cumu_cost)

        sf_cost = sf_cost[::-1]

        ans = []
        for l, r in queries:
            if l == r:
                ans.append(0)
            elif l < r:
                ans.append(pf_cost[r] - pf_cost[l])
            else:
                ans.append(sf_cost[r] - sf_cost[l])

        return ans

nums, queries = [-5,-2,3], [[0,2],[2,0],[1,2]]
nums, queries = [0,2,3,9], [[3,0],[1,2],[2,0]]

Solution().minCost(nums, queries)