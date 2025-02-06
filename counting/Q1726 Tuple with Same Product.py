# counting - medium
import math
class Solution:
    def tupleSameProduct(self, nums):
        
        n = len(nums)

        # use a dict to store the product of all pairs in O(n^2) time
        product_map = dict()

        for i in range(n):
            for j in range(i+1, n):
                currProd = nums[i] * nums[j]
                if currProd not in product_map: product_map[currProd] = 0

                product_map[currProd] += 1

        # every freq. can result in fC2 valid quadruplets, with each quadruplets
        # having 2 * 2^2 = 8 permutations. e.g. suppose we have (1,6), (2,3)
        # 1 & 6 can swap pos., so can 2 & 3, and the two pairs can also swap pos.
        ans = 0
        for _, freq in product_map.items():
            ans += math.comb(freq, 2) * 8

        return ans
    
nums = [2,3,4,6]
nums = [1,2,4,5,10]

Solution().tupleSameProduct(nums)