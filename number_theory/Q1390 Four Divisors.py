# number theory - medium
from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        # to memoize searched number
        cache = dict()

        ans = 0
        for x in nums:

            if x in cache:
                ans += cache[x]
                continue

            # iterate up to sqrt(x) to determine divisors
            res = set()

            for divisor in range(1, int(x**0.5)+1):
                if x % divisor == 0:
                    res.add(divisor)
                    res.add(x // divisor)

                # early stop for exceeding
                if len(res) > 4:
                    break
                
            cache[x] = sum(res) if len(res) == 4 else 0
            ans += cache[x]

        return ans

nums = [21,4,7]
nums = [21,21]
nums = [1,2,3,4,5]

Solution().sumFourDivisors(nums)