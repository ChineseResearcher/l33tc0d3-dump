# greedy - medium
from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        # key ideas:
        # 1) apply greedy thinking and sort first so as to ensure max. value at index n-1
        # 2) conditionally modify values in arr if adjacent diff > 1
        # 3) enforce first value to 1
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]

arr = [2,2,1,2,1]
arr = [1,2,3,4,5]
arr = [100,1,1000]

Solution().maximumElementAfterDecrementingAndRearranging(arr)