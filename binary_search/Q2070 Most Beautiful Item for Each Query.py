# binary search - medium
from typing import List
class Solution:
    def binarySearch(self, prices, query_price):
        n = len(prices)
        l, r = 0, n-1

        while l <= r:

            mid = (l+r) // 2
            if prices[mid] > query_price:
                r = mid - 1

            else:
                l = mid + 1

        return l-1

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices = [x[0] for x in items]
        beauty = [x[1] for x in items]

        cumuMaxBeauty = [beauty[0]]
        for i in range(1, len(beauty)):

            if beauty[i] > cumuMaxBeauty[i-1]:
                cumuMaxBeauty.append(beauty[i])
            else:
                cumuMaxBeauty.append(cumuMaxBeauty[i-1])

        # it is known that items was sorted by increasing prices
        # and break tie by beauty, and thus for each query j, 
        # we can just binary search on the sorted prices and 
        # return the idx of the largest found price <= queries[j]

        ans = []
        for q in queries:

            maxIdx = self.binarySearch(prices, q)
            if maxIdx >= 0:
                ans.append(cumuMaxBeauty[maxIdx])
            else:
                ans.append(0)

        return ans
    
items, queries = [[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]
items, queries = [[1,2],[1,2],[1,3],[1,4]], [1]
items, queries = [[10,1000]], [5]

Solution().maximumBeauty(items, queries)