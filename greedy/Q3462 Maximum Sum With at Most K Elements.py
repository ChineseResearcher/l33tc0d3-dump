# greedy - medium
class Solution:
    def maxSum(self, grid, limits, k):
        m, n = len(grid), len(grid[0])
        # read in the 2-D arr. as flattened, storing row info for ref. to limit
        flattened = [[grid[r][c], r] for r in range(m) for c in range(n)]

        # sort the flattened arr. in desc order and the first k valid elements forms ans.
        flattened.sort(reverse=True)

        ans = 0

        # maintain idx to ref. flattened
        # note that there can be cases where we don't get to select
        idx = 0
        while k > 0:

            while idx < len(flattened) and limits[flattened[idx][1]] == 0:
                idx += 1

            if idx == len(flattened): break
            ans += flattened[idx][0]
            # deplete the limit for the curr. row
            limits[flattened[idx][1]] -= 1
            # move idx pointer to next candidate
            idx += 1
            k -= 1

        return ans
    
grid, limits, k = [[5,3,7],[8,2,6]], [2,2], 3
grid, limits, k = [[1,2],[3,4]], [1,2], 2

Solution().maxSum(grid, limits, k)