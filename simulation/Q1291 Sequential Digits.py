# simulation - medium
from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # key ideas:
        # 1) enumerate starting integer in the form:
        # 1 -> 12 -> 123 -> ... -> 123456789
        # 2 -> 23 -> 234 -> ...

        ans = []
        for i in range(1, 10):

            num, nxtDigit = i, i + 1
            while True:

                if low <= num <= high:
                    ans.append(num)

                if nxtDigit == 10:
                    break

                num = num * 10 + nxtDigit
                nxtDigit += 1

        return sorted(ans)

low, high = 100, 300
low, high = 1000, 13000

Solution().sequentialDigits(low, high)