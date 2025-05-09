# prefix sum - medium
from typing import List
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        # idea is to operate on the sorted beans arr. and build a 
        # prefix sum for efficient computation of  how many beans deletions
        # required if we set nums[i] as the min. all-equal baseline
        beans.sort()

        pfSum, rSum = [], 0
        for i in range(n):
            
            rSum += beans[i]
            pfSum.append(rSum)
            
        ans = float('inf')
        idx = 0

        # we would only need to consider unique beans count in a bag
        while idx < n:
            
            while 0 < idx < n and beans[idx] == beans[idx-1]:
                idx += 1
            
            if idx == n:
                break
            
            # LOGIC:
            # 1) bags with bean count < beans[idx] would all be reduced to 0
            # 2) bags with bean count >= beans[idx] would all be reduced to beans[idx]
            smallerCnt = pfSum[idx-1] if idx > 0 else 0
            largerCnt = pfSum[-1] - pfSum[idx] if idx < n-1 else 0
            
            ans = min(ans, smallerCnt + max(largerCnt - beans[idx]*(n-1-idx), 0))
            
            idx += 1
            
        return ans
    
beans = [4,1,6,5]
beans = [2,10,3,2]

Solution().minimumRemoval(beans)