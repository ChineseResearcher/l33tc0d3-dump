# simulation - medium
import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) simulate as per instructions from the description
        # 2) use prefix max + two pointers

        pf_max, pf_gcd = 0, []
        for x in nums:
            pf_max = fmax(pf_max, x)
            pf_gcd.append(math.gcd(pf_max, x))

        pf_gcd.sort()

        i, j, ans = 0, n - 1, 0
        while i < j:
            ans += math.gcd(pf_gcd[i], pf_gcd[j])
            i += 1
            j -= 1

        return ans

nums = [2,6,4]
nums = [3,6,2,8]

Solution().gcdSum(nums)