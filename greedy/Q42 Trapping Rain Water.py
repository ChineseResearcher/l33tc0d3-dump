# greedy - hard
class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) maintain suffix max
        # 2) bounding height at height[i] is min(prefix[i - 1], suffix[i + 1]) - height[i]
        sfMax = [0] * n

        sfMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            sfMax[i] = fmax(sfMax[i + 1], height[i])

        pfMax, ans = 0, 0
        for i in range(n - 1):
            ans += fmax(fmin(pfMax, sfMax[i + 1]) - height[i], 0)
            pfMax = fmax(pfMax, height[i])

        return ans

height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Solution().trap(height)