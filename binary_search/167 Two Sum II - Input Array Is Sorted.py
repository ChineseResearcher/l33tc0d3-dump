# binary search - medium
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        # key ideas:
        # 1) O(1) space solution needed
        # 2) use binary search for [0, i - 1] for every index i to match target

        for i in range(1, n):
            x = numbers[i]
            y = target - x
            if y > x: continue

            l, r, j = 0, i - 1, -1
            while l <= r:

                mid = (l + r) >> 1
                if numbers[mid] == y:
                    j = mid
                    break
                elif numbers[mid] < y:
                    l = mid + 1
                else:
                    r = mid - 1

            if j != -1:
                return [j + 1, i + 1]

numbers, target = [-1,0], -1
numbers, target = [2,3,4], 6
numbers, target = [2,7,11,15], 9

Solution().twoSum(numbers, target)